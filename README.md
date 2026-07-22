# personal-portfolio

孙新成的个人作品集网站——影像创作者 · 摄影器材玩家 · 军事科技撰稿人。

## 特性

- 🌗 亮色 / 暗色双主题，跟随系统并支持手动切换（localStorage 记忆）
- 📱 全响应式布局，移动端汉堡菜单
- ⚡ 图片已压缩优化（总量从 18.7MB 降至约 1.1MB），封面图懒加载
- 🔍 SEO 完善：meta description、Open Graph、Twitter Card、JSON-LD 结构化数据
- ♿ 可访问性：跳转链接、ARIA 标注、键盘导航、`prefers-reduced-motion` 支持
- ✨ 滚动入场动画、导航滚动高亮、返回顶部

## 项目结构

```
├── index.html          # 页面（引用压缩后的 styles.min.css / main.min.js）
├── styles.css          # 样式源码（编辑此文件）
├── main.js             # 脚本源码（编辑此文件）
├── styles.min.css      # 压缩样式（构建产物，勿直接编辑）
├── main.min.js         # 压缩脚本（构建产物，勿直接编辑）
├── favicon.svg         # 站点图标
├── assets/             # 图片资源
└── tools/
    ├── build.py            # 压缩 CSS/JS 构建脚本
    └── optimize_images.py  # 图片压缩脚本（一次性/新增图片时使用）
```

## 本地预览

```bash
python -m http.server 8000
# 打开 http://localhost:8000
```

## 构建（修改样式/脚本后必做）

`index.html` 引用的是压缩版文件，修改 `styles.css` 或 `main.js` 后需重新构建：

```bash
pip install rcssmin rjsmin   # 首次
python tools/build.py
```

## 新增图片优化

将图片放入 `assets/` 后运行：

```bash
pip install Pillow   # 首次
python tools/optimize_images.py
```

## 部署

静态站点，可直接部署到 GitHub Pages / Gitee Pages / Cloudflare Pages。
