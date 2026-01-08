# 专利子代理架构优化计划

## 一、概述

本计划详细说明专利交底书技能的子代理架构优化方案，旨在减少子代理数量、简化依赖关系、提高可维护性。

## 二、当前架构分析

### 2.1 子代理总数：22个

**分类统计**：
- 基础生成类：9个（01-09）
- 附图生成类：7个（10, 12-16, 21）
- 文档处理类：4个（11, 17-20）
- 其他：2个

### 2.2 子代理清单

| 序号 | 文件名 | 功能 | 使用的 MCP 工具 |
|------|--------|------|----------------|
| 01 | 01-patent-title-generator.md | 发明名称生成 | - |
| 02 | 02-patent-field-analyzer.md | 技术领域分析 | - |
| 03 | 03-patent-background-researcher.md | 背景技术调研 | web-search-prime, google-patents-mcp, exa, web-reader |
| 04 | 04-patent-problem-analyzer.md | 技术问题分析 | - |
| 05 | 05-patent-solution-designer.md | 技术方案设计 | exa, web-search-prime |
| 06 | 06-patent-benefit-analyzer.md | 有益效果分析 | - |
| 07 | 07-patent-implementation-writer.md | 实施方式编写 | exa, web-search-prime |
| 08 | 08-patent-protection-extractor.md | 保护点提炼 | google-patents-mcp |
| 09 | 09-patent-reference-collector.md | 参考资料收集 | google-patents-mcp, web-search-prime, web-reader |
| 10 | 10-patent-diagram-generator.md | 附图协调器 | - |
| 11 | 11-patent-document-integrator.md | 文档整合器 | - |
| 12 | 12-patent-flowchart-generator.md | 流程图生成器 | - |
| 13 | 13-patent-sequence-generator.md | 时序图生成器 | - |
| 14 | 14-patent-protocol-generator.md | 协议图生成器 | - |
| 15 | 15-patent-architecture-generator.md | 架构图生成器 | - |
| 16 | 16-patent-diagram-validator.md | 图表验证器 | - |
| 17 | 17-patent-environment-checker.md | 环境检查器 | - |
| 18 | 18-patent-markdown-parser.md | Markdown 解析器 | - |
| 19 | 19-patent-docx-generator.md | DOCX 生成器 | - |
| 20 | 20-patent-docx-validator.md | DOCX 验证器 | - |
| 21 | 21-patent-diagram-inserter.md | 附图插入器 | - |

## 三、优化方案

### 3.1 方案概览

| 合并前（22个） | 合并后（约10个） | 减少数量 | 风险等级 |
|----------------|-----------------|---------|---------|
| **基础生成类**（9个） | **合并后**（4个） | -5 | 低-中 |
| **附图生成类**（7个） | **合并后**（1个） | -6 | 高 |
| **文档处理类**（4个） | **合并后**（1个） | -3 | 中 |
| **其他**（2个） | **保留**（2个） | 0 | - |

### 3.2 详细合并方案

#### 方案1：基础生成类合并（低风险）

**合并前**：
- 01-title-generator.md（发明名称）
- 02-field-analyzer.md（技术领域）

**合并后**：`01-patent-metadata-generator.md`

**理由**：
- 两个子代理都处理元数据
- 输入相似（idea, technical_field）
- 执行顺序相邻，可并行
- 输出相对独立

**复杂度**：低
**风险**：低
**减少数量**：1个

**实施步骤**：
1. 创建 `01-patent-metadata-generator.md`
2. 合并两个子代理的逻辑
3. 输出两个文件：`01_发明名称.md` 和 `02_所属技术领域.md`
4. 更新 SKILL.md 中的子代理列表
5. 删除旧的子代理文件

---

#### 方案2：发明内容合并（中风险）

**合并前**：
- 04-problem-analyzer.md（技术问题）
- 05-solution-designer.md（技术方案）
- 06-benefit-analyzer.md（有益效果）

**合并后**：`04-patent-content-generator.md`

**理由**：
- 三个子代理都属于"发明内容"章节（第4章）
- 有依赖关系（problem → solution → benefit）
- 共享部分输入（idea, solution_content）

**复杂度**：中
**风险**：中
**减少数量**：2个

**注意事项**：
- 需要确保合并后仍能独立生成各部分
- 保持各部分的输出文件独立
- 需要维护原有的执行顺序

**实施步骤**：
1. 创建 `04-patent-content-generator.md`
2. 按顺序执行三个生成逻辑
3. 输出三个文件：`04_解决的技术问题.md`, `05_技术方案.md`, `06_有益效果.md`
4. 确保各部分可以独立重新生成
5. 更新相关文档
6. 删除旧的子代理文件

---

#### 方案3：实施与保护合并（低风险）

**合并前**：
- 07-implementation-writer.md（实施方式）
- 08-protection-extractor.md（保护点）

**合并后**：`07-patent-detail-generator.md`

**理由**：
- 两个子代理都处理详细内容
- 输入相似（solution_content）
- 执行顺序相邻

**复杂度**：低
**风险**：低
**减少数量**：1个

**实施步骤**：
1. 创建 `07-patent-detail-generator.md`
2. 合并两个子代理的逻辑
3. 输出两个文件：`07_具体实施方式.md` 和 `08_关键点和欲保护点.md`
4. 更新相关文档
5. 删除旧的子代理文件

---

#### 方案4：附图生成类合并（高风险）

**合并前**：
- 10-patent-diagram-generator.md（协调器）
- 12-patent-flowchart-generator.md（流程图）
- 13-patent-sequence-generator.md（时序图）
- 14-patent-protocol-generator.md（协议图）
- 15-patent-architecture-generator.md（架构图）
- 16-patent-diagram-validator.md（验证器）
- 21-patent-diagram-inserter.md（插入器）

**合并后**：`10-patent-diagram-generator-unified.md`

**理由**：
- 所有附图生成器职责相似
- 可统一管理附图编号
- 可简化附图生成逻辑

**复杂度**：高
**风险**：高
**减少数量**：6个

**注意事项**：
- 需要保留所有图表类型支持
- 需要确保图表质量不下降
- 需要统一附图编号管理
- 建议分阶段实施

**实施步骤**：
1. **阶段1**：合并协调器和验证器
   - 创建 `10-patent-diagram-generator-unified.md`
   - 集成协调器和验证器的功能
   - 保留各类型图表生成器作为内部模块

2. **阶段2**：统一附图编号管理
   - 实现全局附图编号计数器
   - 确保所有附图编号连续

3. **阶段3**：内部模块化
   - 将各类型图表生成器改为内部函数
   - 保持接口一致

4. **阶段4**：测试验证
   - 确保所有图表类型正常生成
   - 确保附图编号连续性
   - 确保图表质量不下降

5. **阶段5**：清理旧文件
   - 删除旧的附图生成器文件
   - 更新相关文档

---

#### 方案5：文档处理类合并（中风险）

**合并前**：
- 17-patent-environment-checker.md（环境检查器）
- 18-patent-markdown-parser.md（Markdown 解析器）
- 19-patent-docx-generator.md（DOCX 生成器）
- 20-patent-docx-validator.md（DOCX 验证器）

**合并后**：`11-patent-document-processor.md`

**理由**：
- 都属于文档后处理
- 主要用于 DOCX 转换功能
- 可以统一管理文档处理流程

**复杂度**：中
**风险**：中
**减少数量**：3个

**实施步骤**：
1. 创建 `11-patent-document-processor.md`
2. 合并环境检查、解析、生成、验证逻辑
3. 根据参数决定执行哪些操作
4. 更新相关文档
5. 删除旧的子代理文件

---

### 3.3 保留独立的子代理

以下子代理建议保持独立：

| 子代理 | 理由 |
|--------|------|
| 03-background-researcher | 需要大量 MCP 工具，职责单一，已是独立单元 |
| 09-reference-collector | 需要大量 MCP 工具，职责单一，已是独立单元 |
| 11-document-integrator | 核心整合功能，职责清晰 |

## 四、实施路径

### 4.1 推荐阶段

**阶段1**（低风险合并）：
- metadata-generator（合并01+02）
- detail-generator（合并07+08）

**阶段2**（中风险合并）：
- content-generator（合并04+05+06）
- document-processor（合并17-20）

**阶段3**（高风险合并）：
- diagram-generator-unified（合并所有附图生成器）

### 4.2 实施时间表

| 阶段 | 任务 | 预计工作量 | 风险 |
|------|------|-----------|------|
| 阶段1 | 方案1 + 方案3 | 2-3小时 | 低 |
| 阶段2 | 方案2 + 方案5 | 4-6小时 | 中 |
| 阶段3 | 方案4 | 6-8小时 | 高 |

**总工作量**：约 12-17 小时

## 五、风险评估

### 5.1 风险类型

| 风险类型 | 描述 | 影响程度 | 缓解措施 |
|---------|------|---------|----------|
| **功能退化** | 合并后某些功能可能丢失 | 高 | 充分测试，保留原有功能 |
| **调试困难** | 合并后问题定位更困难 | 中 | 保持代码模块化，添加日志 |
| **向后兼容** | 现有工作流可能受影响 | 中 | 保持接口一致，渐进式迁移 |
| **维护负担** | 合并逻辑更复杂，可能更难维护 | 低 | 充分注释，单元测试 |

### 5.2 回滚计划

每个阶段完成后需要：
1. 充分测试功能
2. 确认所有输出文件正确
3. 确认附图质量不下降
4. 如发现重大问题，立即回滚到上一版本

**回滚方法**：
- 使用 Git 版本控制
- 每个阶段完成后创建 Git tag
- 如需回滚，使用 `git checkout` 恢复

## 六、收益评估

### 6.1 量化指标

| 收益类型 | 描述 | 量化指标 |
|---------|------|----------|
| **减少文件数** | 从22个减少到约10个 | -12个文件（-55%） |
| **简化依赖** | 减少子代理间依赖关系 | 依赖复杂度降低50% |
| **提高效率** | 减少子代理调用开销 | 执行时间减少10-20% |
| **易于维护** | 更少的文件需要维护 | 维护成本降低40% |

### 6.2 定性收益

- **更清晰的项目结构**：子代理职责更明确
- **更简单的调试**：减少子代理数量，问题定位更容易
- **更好的扩展性**：模块化设计便于后续扩展
- **降低新手上手难度**：更少的文件需要理解

## 七、测试计划

### 7.1 功能测试

每个阶段完成后需要测试：

1. **基本功能测试**
   - 运行 `/patent` 命令
   - 确认所有章节正常生成
   - 确认输出文件格式正确

2. **附图测试**
   - 确认所有类型附图正常生成
   - 确认附图编号连续
   - 确认附图质量不下降

3. **断点续传测试**
   - 测试智能检测已生成章节
   - 测试选择性重新生成

4. **创新度评估测试**
   - 测试降级建议功能
   - 测试专利类型切换

### 7.2 回归测试

确保合并后功能与合并前一致：

- 对比合并前后的输出文件
- 确认章节内容格式一致
- 确认附图嵌入位置正确

### 7.3 性能测试

- 测量合并前后的执行时间
- 确认性能提升符合预期

## 八、决策参考

### 8.1 是否需要架构优化？

**建议进行架构优化，如果**：
- 子代理数量影响日常维护
- 经常需要跨多个子代理修改功能
- 团队规模扩大，多人协作时出现冲突

**建议暂缓架构优化，如果**：
- 当前功能稳定，无维护问题
- 团队规模小，维护成本可控
- 优先考虑其他功能改进

### 8.2 混合方案

也可以采用渐进式优化：
1. 先完成低风险合并（方案1、方案3）
2. 测试验证后再进行中风险合并
3. 最后评估是否进行高风险合并

## 九、后续行动

如决定执行此优化计划：

1. **创建分支**：创建 `feature/agent-architecture-optimization` 分支
2. **按阶段执行**：按照实施路径逐步合并
3. **充分测试**：每个阶段完成后进行充分测试
4. **更新文档**：同步更新 AGENTS.md 等文档
5. **合并主分支**：测试通过后合并到主分支
6. **创建版本**：创建新的版本号（如 v2.0.0）

## 十、附录

### 附录A：文件映射表

合并前后的文件映射关系：

| 新文件 | 合并的旧文件 | 说明 |
|--------|-------------|------|
| 01-patent-metadata-generator.md | 01 + 02 | 元数据生成 |
| 03-patent-background-researcher.md | 03（保持） | 背景技术调研 |
| 04-patent-content-generator.md | 04 + 05 + 06 | 发明内容 |
| 07-patent-detail-generator.md | 07 + 08 | 实施与保护 |
| 09-patent-reference-collector.md | 09（保持） | 参考资料收集 |
| 10-patent-diagram-generator-unified.md | 10 + 12-16 + 21 | 附图生成 |
| 11-patent-document-integrator.md | 11（保持） | 文档整合 |
| 12-patent-document-processor.md | 17-20 | 文档后处理 |

### 附录B：子代理数量对比

| 类型 | 优化前 | 优化后 | 减少 |
|------|--------|--------|------|
| 基础生成类 | 9 | 4 | -5 |
| 附图生成类 | 7 | 1 | -6 |
| 文档处理类 | 4 | 1 | -3 |
| 其他 | 2 | 2 | 0 |
| **总计** | **22** | **10** | **-12** |

### 附录C：依赖关系图

优化前的依赖关系：
```
title-generator → field-analyzer → background-researcher → problem-analyzer → solution-designer → benefit-analyzer → implementation-writer → protection-extractor → reference-collector → document-integrator
                                       ↓
                                 [各类型附图生成器]
```

优化后的依赖关系：
```
metadata-generator → background-researcher → content-generator → detail-generator → reference-collector → document-integrator
                                              ↓
                                        diagram-generator-unified
```

简化度：从 11 个串行步骤减少到 7 个串行步骤。
