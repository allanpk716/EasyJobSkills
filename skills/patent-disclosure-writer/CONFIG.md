# MCP 服务配置指南

本指南详细说明如何配置专利交底书技能所需的 MCP 服务。

## 概述

专利交底书技能依赖以下 MCP 服务：

| MCP 服务 | 用途 | 必需 |
|---------|------|------|
| web-search-prime | 网络搜索 | ✅ 是 |
| web-reader | 网页内容提取 | ✅ 是 |
| google-patents-mcp | 专利检索 | ✅ 是 |
| exa | 技术文档搜索 | ✅ 是 |

## 配置步骤

### 步骤 1：获取 API 密钥

你需要获取以下 API 密钥：

| 服务 | 获取地址 | 费用 |
|------|---------|------|
| 智谱 API（web-search-prime/web-reader） | https://open.bigmodel.cn/ | 有免费额度 |
| SerpAPI（google-patents-mcp） | https://serpapi.com/ | 有免费额度 |
| Exa API（exa） | https://exa.ai/api-key | 有免费额度 |

**获取步骤**：

1. 访问对应的网站
2. 注册账号
3. 在账号设置中生成 API 密钥
4. 保存 API 密钥（后续配置需要）

### 步骤 2：配置 MCP 服务

在 `~/.claude/settings.json` 或项目的 `.claude.json` 中添加 MCP 服务配置：

#### Windows 配置示例

```json
{
  "mcpServers": {
    "web-search-prime": {
      "type": "http",
      "url": "https://open.bigmodel.cn/api/mcp/web_search_prime/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ZHIPU_API_KEY"
      }
    },
    "web-reader": {
      "type": "http",
      "url": "https://open.bigmodel.cn/api/mcp/web_reader/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ZHIPU_API_KEY"
      }
    },
    "google-patents-mcp": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@kunihiros/google-patents-mcp"
      ],
      "env": {
        "SERPAPI_API_KEY": "YOUR_SERPAPI_KEY"
      }
    },
    "exa": {
      "type": "stdio",
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "exa-mcp-server"
      ],
      "env": {
        "EXA_API_KEY": "YOUR_EXA_API_KEY"
      }
    }
  }
}
```

#### macOS/Linux 配置示例

```json
{
  "mcpServers": {
    "web-search-prime": {
      "type": "http",
      "url": "https://open.bigmodel.cn/api/mcp/web_search_prime/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ZHIPU_API_KEY"
      }
    },
    "web-reader": {
      "type": "http",
      "url": "https://open.bigmodel.cn/api/mcp/web_reader/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ZHIPU_API_KEY"
      }
    },
    "google-patents-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@kunihiros/google-patents-mcp"
      ],
      "env": {
        "SERPAPI_API_KEY": "YOUR_SERPAPI_KEY"
      }
    },
    "exa": {
      "command": "npx",
      "args": [
        "-y",
        "exa-mcp-server"
      ],
      "env": {
        "EXA_API_KEY": "YOUR_EXA_API_KEY"
      }
    }
  }
}
```

**重要**：
- 将 `YOUR_ZHIPU_API_KEY` 替换为你的智谱 API 密钥
- 将 `YOUR_SERPAPI_KEY` 替换为你的 SerpAPI 密钥
- 将 `YOUR_EXA_API_KEY` 替换为你的 Exa API 密钥
- Windows 使用 `cmd /c`，macOS/Linux 直接使用 `npx`

### 步骤 3：验证配置

配置完成后，在 Claude Code 中运行以下命令验证 MCP 服务是否正常：

```bash
# 查看已加载的 MCP 服务
/mcp list
```

确保以下工具可用：

| MCP服务 | 工具名称 |
|---------|----------|
| web-search-prime | `mcp__web-search-prime__webSearchPrime` |
| web-reader | `mcp__web_reader__webReader` |
| google-patents-mcp | `mcp__google-patents-mcp__search_patents` |
| exa | `mcp__exa__get_code_context_exa` |

## 常见配置问题

### 问题 1：MCP 服务未加载

**症状**：`/mcp list` 中看不到对应的服务

**解决方案**：
1. 检查 `settings.json` 文件路径是否正确
   - Windows: `C:\Users\<用户名>\.claude\settings.json`
   - macOS/Linux: `~/.claude/settings.json`
2. 检查 JSON 格式是否正确（使用 JSON 验证工具）
3. 重启 Claude Code

### 问题 2：API 密钥无效

**症状**：服务已加载但调用时报错"认证失败"

**解决方案**：
1. 确认 API 密钥已正确复制（没有多余空格）
2. 确认 API 密钥未过期
3. 确认账户有可用额度

### 问题 3：npx 命令未找到

**症状**：google-patents-mcp 或 exa 服务启动失败

**解决方案**：
1. 确认已安装 Node.js（运行 `node --version` 检查）
2. 如未安装，从 https://nodejs.org/ 下载安装
3. 重启 Claude Code

### 问题 4：网络连接问题

**症状**：MCP 服务超时或连接失败

**解决方案**：
1. 检查网络连接
2. 如使用代理，配置 Node.js 代理设置
3. 尝试手动运行 npx 命令测试

## 环境变量配置（可选）

如果你不想在配置文件中硬编码 API 密钥，可以使用环境变量：

### Windows

```powershell
# 在 PowerShell 中设置
$env:ZHIPU_API_KEY="your_key_here"
$env:SERPAPI_KEY="your_key_here"
$env:EXA_API_KEY="your_key_here"
```

### macOS/Linux

```bash
# 在 ~/.bashrc 或 ~/.zshrc 中添加
export ZHIPU_API_KEY="your_key_here"
export SERPAPI_KEY="your_key_here"
export EXA_API_KEY="your_key_here"
```

然后在配置文件中使用：

```json
{
  "env": {
    "ZHIPU_API_KEY": "${ZHIPU_API_KEY}",
    "SERPAPI_KEY": "${SERPAPI_KEY}",
    "EXA_API_KEY": "${EXA_API_KEY}"
  }
}
```

## 项目级配置（推荐）

如果你想在项目中配置 MCP 服务（而不是全局配置），可以在项目根目录创建 `.claude.json` 文件：

```json
{
  "mcpServers": {
    // ... 同上配置
  }
}
```

项目级配置会覆盖全局配置，适合团队协作。

## 下一步

配置完成后，你就可以开始使用专利交底书技能了：

1. 运行 `/patent` 开始生成交底书
2. 如遇到问题，查看 [故障排查指南](TROUBLESHOOTING.md)
