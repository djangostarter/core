# DjangoStarter Core（django-starter-core）

`django-starter-core` 是 DjangoStarter 生态的共享核心库（Core）：把 “模板项目里会重复出现、但又希望长期稳定/可升级的底座能力” 统一沉淀为一个可复用的 Python 包，供：

- 全栈项目：`django-starter-web`
- API-only 项目：`django-starter-api`

共同依赖与复用。

> 包名与 import 命名空间说明：
>
> - 安装包名（PyPI / 依赖声明）：`django-starter-core`
> - Python import 命名空间：`django_starter_core`

## 设计目标

- **可升级**：Core 以版本化发布为中心（SemVer），Web/API 通过升级依赖版本跟进框架升级。
- **可插拔**：Core 内置一系列可选 Django apps（contrib），项目按需启用，避免“一刀切”耦合。
- **强约定**：对外提供稳定的集成点（settings 结构、urls/router 组织、通用响应格式等），减少用户自定义 glue code。

## 能力概览

Core 的代码主要分为两层：

- **基础层（framework utilities）**
  - 基类模型：软删除 + 创建/更新时间戳（见 `django_starter_core.db.models.ModelExt`）
  - 统一响应封装：面向 Django-Ninja 的响应生成（见 `django_starter_core.http.response.responses`）
  - 常用常量/工具：`constants.py`、`utilities.py`
- **可选能力（Django contrib apps）**
  - 鉴权：JWT 生成/解析、Bearer 鉴权（`django_starter_core.contrib.auth.*`）
  - 验证码：验证码相关 API/服务（`django_starter_core.contrib.captcha.*`）
  - 配置中心：配置项管理与 API（`django_starter_core.contrib.config.*`）
  - 监控：Prometheus metrics 与相关中间件/页面/接口（`django_starter_core.contrib.monitoring.*`）
  - 代码生成：根据模型生成 CRUD/Ninja schemas/tests 的管理命令（`django_starter_core.contrib.code_generator.*`）
  - 种子数据：自动生成开发用假数据（`django_starter_core.contrib.seed.*`）
  - Web 侧通用页面/组件（供全栈项目复用）：docs、guide、about、navbar、notifications、admin 等

## 版本与运行环境

- Python：`django-starter-core` 要求 `>=3.12`（见 `pyproject.toml`）
- Django：依赖 `django>=6.0`
- API 框架：`django-ninja>=1.5.3`、`pydantic>=2`

## 安装与使用

### 作为依赖安装（推荐：用户侧）

在你的项目里声明依赖即可：

- `pip`：

  ```bash
  pip install django-starter-core
  ```

- `uv`：

  ```bash
  uv add django-starter-core
  ```

### 本地可编辑联调（推荐：Core 开发者侧）

如果你在同一工作区同时开发 `core` 与 `web/api`，建议使用 “本地路径 editable 覆盖” 来获得最顺滑的联调体验：

- 你对 `django_starter_core` 的任何改动都会立刻在 web/api 中生效
- 断点调试/单步调试与普通源码项目一致
- 不需要等待发布到 PyPI

`django-starter-api` 已经默认配置了 uv 的本地覆盖（见其 `pyproject.toml`）：

```toml
[tool.uv.sources]
django-starter-core = { path = "../django-starter-core", editable = true }
```

## 集成指南

Core 的能力大多是“可选启用”，因此集成时你通常只需要做三件事：

1. 安装依赖
2. 按需加入 `INSTALLED_APPS`
3. 按需挂载 urls / Ninja router

### 1）按需启用 Django apps

在项目的 `INSTALLED_APPS` 中添加你需要的模块，例如：

```python
INSTALLED_APPS = [
    # Django 内置
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Core 可选模块（举例）
    "django_starter_core.contrib.auth",
    "django_starter_core.contrib.captcha",
    "django_starter_core.contrib.config",
    "django_starter_core.contrib.monitoring",
]
```

启用后按常规方式迁移数据库即可：

```bash
python manage.py migrate
```

### 2）挂载 Core 提供的页面型 URLs（全栈项目常用）

Core 提供了一个聚合 urls（主要用于全栈项目复用文档页/引导页/通知等）：

```python
from django.urls import include, path

urlpatterns = [
    path("", include("django_starter_core.urls")),
]
```

默认会包含（具体见 `django_starter_core/urls.py`）：

- `/`：guide
- `/about/`：about
- `/docs/`：docs
- `/notifications/`：notifications
- `/admin/`：admin 相关扩展

API-only 项目一般不需要挂载这些页面型 urls，可忽略。

### 3）挂载 Core 提供的 Ninja Router（API 项目常用）

Core 提供了一个聚合 router（验证码、配置中心、监控等）：

```python
from ninja import NinjaAPI
from django_starter_core.apis import router as core_router

api = NinjaAPI()
api.add_router("/core", core_router)
```

## JWT 配置约定

Core 的 JWT 逻辑默认读取 `settings.DJANGO_STARTER['auth']['jwt']`：

```python
DJANGO_STARTER = {
    "auth": {
        "jwt": {
            "algo": "HS256",
            "salt": "...",      # 强随机密钥，务必通过环境变量注入
            "lifetime": 3600,   # 秒
        }
    }
}
```

`django-starter-api` 已内置同结构配置与环境变量约定，你可以直接复用。

## 开发与测试（Core 仓库）

Core 使用 `pyproject.toml` 管理依赖，并提供基础测试用例：

```bash
uv sync
uv run pytest
```

## 生态关系与分发形态

- Core：提供可复用底座能力（本仓库，建议独立版本化发布）
- API：API-only 项目模板，依赖 Core（`django-starter-api`）
- Web：全栈项目模板，依赖 Core（`django-starter-web`）

这一拆分的核心价值是：**Web/API 的用户升级体验变成“升级 Core 版本 + 按 changelog 做极少量调整”**，而不是把底座能力复制到每个模板里反复维护。
