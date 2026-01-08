# 故障排查指南

本文档提供专利交底书技能使用过程中常见问题的解决方案。

## 目录

- [MCP 服务相关问题](#mcp-服务相关问题)
- [命令执行问题](#命令执行问题)
- [生成质量问题](#生成质量问题)
- [文件和目录问题](#文件和目录问题)
- [附图相关问题](#附图相关问题)
- [DOCX 转换问题](#docx-转换问题)

---

## MCP 服务相关问题

### 问题 1：MCP 服务未加载

**症状**：
- 运行 `/mcp list` 看不到 MCP 服务
- 执行命令时提示"工具不可用"

**可能原因**：
1. 配置文件路径错误
2. JSON 格式错误
3. Claude Code 未重启

**解决方案**：

1. **检查配置文件路径**：
   - Windows: `C:\Users\<用户名>\.claude\settings.json`
   - macOS/Linux: `~/.claude/settings.json`

2. **验证 JSON 格式**：
   使用在线 JSON 验证工具检查格式是否正确

3. **重启 Claude Code**：
   ```bash
   # 完全退出 Claude Code 后重新打开
   ```

4. **查看错误日志**：
   ```bash
   /mcp list
   ```
   查看具体哪个服务加载失败

---

### 问题 2：API 密钥无效

**症状**：
- MCP 服务已加载但调用时报错"认证失败"
- 提示"Unauthorized"或"401"

**可能原因**：
1. API 密钥复制错误（多余空格）
2. API 密钥已过期
3. 账户余额不足

**解决方案**：

1. **重新复制 API 密钥**：
   - 确保没有前后空格
   - 确保复制完整的密钥

2. **验证 API 密钥**：
   ```bash
   # 测试智谱 API
   curl -H "Authorization: Bearer YOUR_KEY" https://open.bigmodel.cn/api/paas/v4/chat/completions
   ```

3. **检查账户余额**：
   - 登录各服务官网确认额度充足

---

### 问题 3：网络连接超时

**症状**：
- MCP 服务调用超时
- 提示"Network error"或"Timeout"

**可能原因**：
1. 网络连接不稳定
2. 防火墙/代理设置问题
3. MCP 服务端故障

**解决方案**：

1. **检查网络连接**：
   ```bash
   ping open.bigmodel.cn
   ping serpapi.com
   ```

2. **配置代理**（如需要）：
   ```json
   {
     "env": {
       "HTTP_PROXY": "http://proxy.example.com:8080",
       "HTTPS_PROXY": "http://proxy.example.com:8080"
     }
   }
   ```

3. **手动测试 MCP 服务**：
   ```bash
   npx -y @kunihiros/google-patents-mcp
   ```

---

### 问题 4：npx 命令未找到

**症状**：
- google-patents-mcp 或 exa 服务启动失败
- 提示"npx: command not found"

**解决方案**：

1. **检查 Node.js 安装**：
   ```bash
   node --version
   npm --version
   ```

2. **安装 Node.js**：
   - 访问 https://nodejs.org/
   - 下载并安装 LTS 版本

3. **重启终端**：
   - 安装后需要重启终端使环境变量生效

---

## 命令执行问题

### 问题 5：/patent 命令无响应

**症状**：
- 运行 `/patent` 没有任何反应
- 没有提示输入信息

**可能原因**：
1. 技能未正确加载
2. 命令拼写错误
3. Claude Code 未加载插件

**解决方案**：

1. **验证技能已加载**：
   ```bash
   /agents
   ```
   查看是否能看到专利相关子代理

2. **检查命令拼写**：
   - 确保是 `/patent` 不是 `patent` 或 `/patents`

3. **重新加载插件**：
   ```bash
   # 重新启动 Claude Code
   ```

---

### 问题 6：子代理调用失败

**症状**：
- 执行过程中某个子代理失败
- 提示"Agent execution failed"

**可能原因**：
1. 子代理文件不存在
2. 子代理配置格式错误
3. MCP 工具不可用

**解决方案**：

1. **检查子代理文件**：
   ```bash
   ls agents/patent/*.md
   ```
   确保所有 11 个子代理文件存在

2. **查看子代理配置**：
   - 验证 YAML frontmatter 格式正确

3. **检查 MCP 工具**：
   ```bash
   /mcp list
   ```
   确保所需的 MCP 工具可用

---

## 生成质量问题

### 问题 7：生成内容不完整

**症状**：
- 某些章节内容过短
- 缺少关键信息

**解决方案**：

1. **提供更详细的创新想法**：
   - 增加技术细节描述
   - 说明技术原理和实现方式

2. **提供准确的关键词**：
   - 选择 3-5 个核心技术关键词
   - 避免使用过于宽泛的词

3. **选择正确的专利类型**：
   - 确保专利类型与创新内容匹配

4. **重新生成特定章节**：
   ```bash
   /patent
   # 选择"选择特定章节重新生成"
   ```

---

### 问题 8：技术方案描述不准确

**症状**：
- 生成的技术方案与实际想法有偏差
- 技术细节描述错误

**解决方案**：

1. **使用更精确的技术术语**
2. **提供技术实现参考**：
   - 可以在创新想法中提及类似的技术方案
3. **手动编辑生成的章节**：
   - 直接编辑 Markdown 文件
   - 重新运行 `/patent` 整合文档

---

## 文件和目录问题

### 问题 9：输出目录不存在

**症状**：
- 提示"目录不存在"
- 文件保存失败

**解决方案**：

1. **手动创建输出目录**：
   ```bash
   mkdir output
   ```

2. **使用绝对路径**：
   ```
   输出目录: C:\WorkSpace\专利\output
   ```

3. **检查目录权限**：
   - 确保有写入权限

---

### 问题 10：章节文件丢失

**症状**：
- 某些章节文件没有生成
- 整合文档时提示文件不存在

**解决方案**：

1. **检查工作目录**：
   ```bash
   ls [0-9][0-9]_*.md
   ```
   查看哪些章节文件存在

2. **重新生成缺失章节**：
   ```bash
   /patent
   # 选择"选择特定章节重新生成"
   ```

3. **使用断点续传**：
   - 技能会自动检测缺失章节并补全

---

## 附图相关问题

### 问题 11：附图编号不连续

**症状**：
- 附图编号跳号（如：图1, 图2, 图4）
- 缺少某些编号

**解决方案**：

1. **运行附图更新命令**：
   ```bash
   /patent-update-diagrams
   ```
   该命令会自动修复编号问题

2. **手动重新编号**：
   - 编辑章节文件
   - 调整附图编号使其连续

3. **重新生成所有附图**：
   ```bash
   /patent-update-diagrams --force_regenerate
   ```

---

### 问题 12：Mermaid 图表无法渲染

**症状**：
- 附图显示为代码块而不是图形
- 编辑器不支持 Mermaid

**解决方案**：

1. **使用支持 Mermaid 的编辑器**：
   - Typora
   - VS Code（安装 Mermaid 插件）
   - Obsidian

2. **在线渲染**：
   - 访问 https://mermaid.live/
   - 粘贴 Mermaid 代码查看渲染效果

3. **转换为 DOCX**：
   ```bash
   /patent-md-2-docx
   ```
   DOCX 格式会自动将 Mermaid 转换为图片

---

### 问题 13：附图内容不正确

**症状**：
- 生成的附图与技术内容不匹配
- 附图过于复杂或过于简单

**解决方案**：

1. **使用 `/patent-update-diagrams` 重新生成特定附图**
2. **手动编辑 Mermaid 代码**：
   - Mermaid 语法简单，可以直接修改
   - 参考 [Mermaid 文档](https://mermaid.js.org/)
3. **联系技术支持**：
   - [GitHub Issues](https://github.com/allanpk716/EasyJobSkills/issues)

---

## DOCX 转换问题

### 问题 14：DOCX 转换失败

**症状**：
- 运行 `/patent-md-2-docx` 报错
- 提示"python-docx not found"

**解决方案**：

1. **安装 python-docx**：
   ```bash
   pip install python-docx
   ```

2. **检查 Python 环境**：
   ```bash
   python --version
   ```

3. **验证安装**：
   ```bash
   python -c "import docx; print(docx.__version__)"
   ```

---

### 问题 15：Mermaid 图表未转换

**症状**：
- DOCX 文件中附图仍然是代码块
- 没有转换为图片

**解决方案**：

1. **安装 mermaid-cli**：
   ```bash
   npm install -g @mermaid-js/mermaid-cli
   ```

2. **安装中文字体**：
   - 下载 [思源黑体 CN](https://github.com/adobe-fonts/source-han-sans/releases)
   - Windows：右键安装
   - macOS：双击安装

3. **验证安装**：
   ```bash
   mmdc --version
   ```

---

### 问题 16：DOCX 格式错乱

**症状**：
- DOCX 文档格式不正确
- 章节编号或标题格式错误

**解决方案**：

1. **检查 Markdown 格式**：
   - 确保章节编号格式正确
   - 确保标题层级正确

2. **手动调整 Word 格式**：
   - 在 Word 中调整样式
   - 使用"格式刷"统一格式

3. **使用模板**：
   - 确保模板文件 `发明、实用新型专利申请交底书 模板.docx` 存在

---

## 其他问题

### 问题 17：创新度评估不准确

**症状**：
- 建议的专利类型不合适
- 创新度评估结果与预期不符

**解决方案**：

1. **提供更详细的关键词**
2. **选择正确的专利类型**：
   - 在输入时明确指定专利类型
3. **忽略建议**：
   - 如果坚持原专利类型，可以在询问时选择"维持发明专利"

---

### 问题 18：生成速度慢

**症状**：
- 生成过程超过 30 分钟
- 某个子代理执行时间过长

**可能原因**：
1. 网络速度慢
2. MCP 服务响应慢
3. 创新想法过于复杂

**解决方案**：

1. **检查网络连接**
2. **简化创新想法描述**：
   - 聚焦核心技术点
   - 避免过多细节
3. **使用断点续传**：
   - 避免每次都重新生成所有章节

---

### 问题 19：内存不足

**症状**：
- Claude Code 崩溃
- 提示"Out of memory"

**解决方案**：

1. **分批生成**：
   - 使用断点续传功能
   - 避免一次性处理太多章节

2. **清理输出目录**：
   ```bash
   # 备份后清理旧的输出文件
   ```

3. **重启 Claude Code**：
   - 定期重启释放内存

---

## 获取帮助

如果以上方案都无法解决你的问题，请：

1. **查看详细日志**：
   - Claude Code 的错误日志
   - MCP 服务的日志

2. **收集信息**：
   - 具体的错误信息
   - 操作步骤
   - 系统环境（OS、Claude Code 版本）

3. **联系支持**：
   - [GitHub Issues](https://github.com/allanpk716/EasyJobSkills/issues)
   - 描述问题并附上错误日志

---

## 常用诊断命令

```bash
# 检查 MCP 服务
/mcp list

# 检查子代理
/agents

# 检查技能
/skills

# 查看帮助
/help
```
