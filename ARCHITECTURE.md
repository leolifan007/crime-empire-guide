# Crime Empire Guide — Site Architecture (Product Design)

## User Flow

```
首页 → 浏览Hero(6款游戏) → 点击游戏卡展开 → 下方面板自动切换
     ↓
  游戏面板 → 指南卡片(游戏特色图标+标签) → 点击卡片
     ↓
  单页指南 → 面包屑导航 → 左侧本游戏目录 → 上下篇导航 → 返回游戏
```

## Navigation Layer

```
[Header: CRIME EMPIRE | Schedule I | Drug Lord | DDS 2 | Crime Boss | Mafia Biz | Underworld]
[Breadcrumb: Home > Schedule I > Best Recipe Rankings]
```

- **始终固定顶部导航** 6款游戏快速跳转
- **面包屑** 每页显示完整路径
- **指南页面左侧栏** 展示本游戏全部指南列表（高亮当前）
- **上下篇按钮** 底部 Prev / Next

## Content Layer

| 层级 | 页面 | 渲染方式 |
|------|------|----------|
| 1 | 首页 | `home.html` — Hero+内容面板 |
| 2 | 游戏页 | `section list.html` — 该游戏全部指南 |
| 3 | 指南页 | `single.html` — 全文+导航 |

## Visual Identity Per Game

| Game | Accent Color | Theme Icon |
|------|-------------|------------|
| Schedule I | gold `#d4a843` | 💊 drugs |
| Drug Lord Tycoon | orange `#e07b3a` | 🏛️ empire |
| DDS 2 | cyan `#2ecc9a` | 💀 skull |
| Crime Boss | red `#c0392b` | 🔥 fire |
| Mafia Biz | purple `#8e44ad` | 🤵 suit |
| Underworld | teal `#1abc9c` | 👁️ eye |
