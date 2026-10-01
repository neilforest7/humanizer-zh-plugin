# 讲人话

把 [humanizer-zh](humanizer-zh/skills/humanizer-zh/SKILL.md) 完整打包为插件。润色中文文章、评论和文档，处理空话、重复及模板化表达，保留事实、确定程度、文体与作者声音。

免费，无购买功能。发布者：[neilforest7](https://github.com/neilforest7)。

## 安装

在支持插件的 Codex CLI 中执行：

```sh
codex plugin marketplace add neilforest7/humanizer-zh-plugin
codex plugin add humanizer-zh@humanizer-zh-plugins
```

安装后，在新对话里选择「讲人话」，粘贴待润色的文字。插件技术名称为 `humanizer-zh`，中文显示名为「讲人话」。

[下载插件 ZIP](https://github.com/neilforest7/humanizer-zh-plugin/releases/latest)。公开 GitHub 发布和 OpenAI 公共目录上架分别处理；以目录中的实际审核状态为准。

## 使用

> 请用讲人话润色下面的中文，保留事实、确定程度和我的语气。

> 请用讲人话审阅这篇文章，只给修改建议。

> 请用讲人话润色这个文件的正文，保留代码、链接、数据和标题结构。

可以附作者样本。默认交付最终稿；只有用户要求修改文件时才写回。已经清楚自然的句子可以保留原样。不能判断作者身份，也不保证通过 AI 检测器。

## 来源与许可

技能正文沿用 humanizer-zh 的 2026-09-23 修订版，未改写，包含全部 31 条模式和原有来源链接。

- [blader/humanizer v3.0.0](https://github.com/blader/humanizer/blob/v3.0.0/SKILL.md)
- [Humanizer-zh PR 39](https://github.com/op7418/Humanizer-zh/pull/39)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)

沿用 [MIT 许可](LICENSE)，保留原版权声明。

## 打包

```sh
python3 scripts/package.py
```

生成 `dist/humanizer-zh-1.0.0.zip`，并核验包内原文、许可、图标和目录结构。

安装方式参考 [OpenAI 官方插件文档](https://developers.openai.com/plugins/build/plugins)。
