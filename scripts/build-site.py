"""Generate the English and Chinese static resume pages."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://liutianjie.github.io'
GITHUB = 'https://github.com/LiuTianjie'

COPY = {
 'en': {
  'lang':'en','file':'index.html','name':'Liu Tao','subtitle':'Software engineer / Product builder',
  'title':'Liu Tao — Software engineer & product builder',
  'description':'Liu Tao: software engineer and product builder working in AI education, native apps, and developer tools. Previously at ByteDance, Alibaba Cloud, and Intel.',
  'intro':'I’m Liu Tao, also known as Nickname4th. I am a software engineer and product builder, currently working in AI education.',
  'previous':'Previously at','experience':'as a software / senior frontend engineer. My work has focused on frontend engineering, product experience, and developer productivity.',
  'focus':'I also build and maintain my own tools. Recent projects explore remote coding-agent workspaces, mobile-device automation, on-device voice input, and self-hosted deployment.',
  'approach':'I enjoy working across the whole product: the interface people use, the systems behind it, and the details that make it reliable in everyday use.',
  'work':'Selected projects','work_intro':'Tools I build and maintain. Each repository includes its own setup instructions, platform support, and license.',
  'projects':[
   ('LinkShell','Remote access to local terminals and coding agents from a phone or browser.','https://liutianjie.github.io/LinkShell/','/img/linkshell-icon.png'),
   ('StupidMirror','Native iOS and Android mirroring on macOS, with a local MCP interface for device automation.','https://liutianjie.github.io/StupidMirror/','/img/projects/stupidmirror-icon.webp'),
   ('Luma','A self-hosted deployment control plane for containers, built on Nomad.','https://liutianjie.github.io/luma/','/img/projects/luma-icon.png'),
   ('Saylane','A macOS input method for on-device dictation, Pinyin, and translation.','https://liutianjie.github.io/Saylane/','/img/projects/saylane-icon.png'),
   ('pura','A shared Android device workspace for team reviews, control, and annotated feedback.','https://liutianjie.github.io/pura/','/img/projects/pura-icon.png'),
   ('gitea-review-agent','Self-hosted AI code reviews and alert analysis for Gitea.','https://github.com/LiuTianjie/gitea-review-agent','')],
  'other':'Other work','others':[
   ('BrowserDisplay','Use a browser as a local Mac display.','https://liutianjie.github.io/BrowserDisplay/'),
   ('1Doc','A multilingual mirror and index for public documentation.','https://github.com/LiuTianjie/1Doc'),
   ('Pencil Box','A learning growth and career planning platform.','https://gaojiua.com/'),
   ('iTool','An online toolbox for developers, designers, and knowledge workers.','https://itool.tech')],
  'stack':'Technical focus','stack_text':'My recent work uses TypeScript, React, Vue, Expo / React Native, Swift, Python, and Go. I use Docker and Nomad for self-hosted services.',
  'now':'Current interests','now_text':'I am exploring how AI can support learning and everyday development: working with real devices, giving useful feedback, and helping people turn an idea into something they can try.',
  'contact':'Find me','contact_text':'For product feedback or technical questions, an issue in the relevant repository is the best place to start.',
  'support':'Support my work','wechat':'WeChat','wechat_alt':'WeChat contact QR code for Liu Tao','github_alt':'GitHub profile QR code for Liu Tao','skip':'Skip to content',
 },
 'zh': {
  'lang':'zh-CN','file':'zh.html','name':'刘涛 · Liu Tao','subtitle':'软件工程师 / 产品开发者',
  'title':'刘涛 Liu Tao — 软件工程师与产品开发者',
  'description':'刘涛的个人主页：软件工程师与产品开发者，关注 AI 教育、原生应用和开发工具。曾在字节跳动、阿里云和 Intel 工作。',
  'intro':'我是刘涛，也使用 Nickname4th 这个名字。我是一名软件工程师和产品开发者，目前在 AI 教育领域创业。',
  'previous':'曾在','experience':'从事软件及高级前端工程工作，长期关注前端工程、产品体验和开发效率。',
  'focus':'我也持续构建和维护自己的工具，近期主要涉及编程 Agent 的远程工作台、移动真机自动化、端侧语音输入和自托管部署。',
  'approach':'我喜欢完整地参与一个产品：从用户接触的界面，到背后的系统实现，再到日常使用中的稳定性与细节。',
  'work':'代表项目','work_intro':'以下项目由我持续开发和维护。各仓库分别提供安装说明、支持平台和许可证。',
  'projects':[
   ('LinkShell','在手机或浏览器中，远程使用本机终端与编程 Agent。','https://liutianjie.github.io/LinkShell/','/img/linkshell-icon.png'),
   ('StupidMirror','在 macOS 上镜像 iOS / Android 真机，通过本地 MCP 接入设备自动化。','https://liutianjie.github.io/StupidMirror/','/img/projects/stupidmirror-icon.webp'),
   ('Luma','基于 Nomad 的自托管容器部署控制面。','https://liutianjie.github.io/luma/','/img/projects/luma-icon.png'),
   ('Saylane','macOS 原生输入法，支持端侧听写、拼音和翻译。','https://liutianjie.github.io/Saylane/','/img/projects/saylane-icon.png'),
   ('pura','团队共享 Android 真机，进行评审、操作并记录带标注的反馈。','https://liutianjie.github.io/pura/','/img/projects/pura-icon.png'),
   ('gitea-review-agent','为 Gitea 自托管 AI 代码审查与告警分析。','https://github.com/LiuTianjie/gitea-review-agent','')],
  'other':'其他作品','others':[
   ('BrowserDisplay','将浏览器变成本地 Mac 扩展显示器。','https://liutianjie.github.io/BrowserDisplay/'),
   ('1Doc','公共技术文档的多语言镜像与索引。','https://github.com/LiuTianjie/1Doc'),
   ('笔袋','学习成长与生涯规划平台。','https://gaojiua.com/'),
   ('iTool','面向开发者、设计师和知识工作者的在线工具箱。','https://itool.tech')],
  'stack':'技术方向','stack_text':'近期主要使用 TypeScript、React、Vue、Expo / React Native、Swift、Python 和 Go，通过 Docker 与 Nomad 部署自托管服务。',
  'now':'目前关注','now_text':'我在探索 AI 如何进入学习与日常开发：操作真实设备、提供有用的反馈，以及帮助人们把想法变成可以亲手尝试的东西。',
  'contact':'联系我','contact_text':'产品反馈或技术问题，欢迎在对应仓库提 Issue，方便围绕具体问题展开讨论。',
  'support':'支持我的工作','wechat':'微信','wechat_alt':'刘涛的微信联系二维码','github_alt':'刘涛的 GitHub 主页二维码','skip':'跳到正文',
 }
}

def render(c):
 chinese=c['lang']=='zh-CN'
 canonical=BASE+('/zh.html' if chinese else '/')
 projects='\n'.join(f'''      <a class="project-item" href="{url}">
        {f'<img src="{image}" width="36" height="36" alt="" />' if image else '<span class="project-initial" aria-hidden="true">GR</span>'}
        <span><strong>{name}</strong><span class="project-description">{description}</span></span>
      </a>''' for name,description,url,image in c['projects'])
 others='\n'.join(f'      <li><a href="{url}">{name}</a> — {description}</li>' for name,description,url in c['others'])
 return f'''<!doctype html>
<html lang="{c['lang']}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#ffffff" />
  <meta name="description" content="{c['description']}" />
  <meta name="author" content="Liu Tao" />
  <meta property="og:title" content="{c['title']}" />
  <meta property="og:description" content="{c['description']}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta name="twitter:card" content="summary" />
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="en" href="{BASE}/" />
  <link rel="alternate" hreflang="zh-CN" href="{BASE}/zh.html" />
  <link rel="alternate" hreflang="x-default" href="{BASE}/" />
  <link rel="icon" href="/img/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/css/main.css?v=20260926-resume" />
  <title>{c['title']}</title>
</head>
<body>
<a class="skip-link" href="#main">{c['skip']}</a>
<main class="page" id="main">
  <nav class="language-nav" aria-label="Language"><a href="/" lang="en"{' aria-current="page"' if not chinese else ''}>English</a><span aria-hidden="true">/</span><a href="/zh.html" lang="zh-CN"{' aria-current="page"' if chinese else ''}>中文</a></nav>
  <section class="intro" id="about" aria-labelledby="title">
    <h1 id="title">{c['name']}</h1>
    <p class="subtitle">{c['subtitle']}</p>
    <p>{c['intro']}</p>
    <p class="experience">{c['previous']}
      <a class="company" href="https://www.bytedance.com/"><img src="/img/company/bytedance-icon.png" alt="" /><span>{'字节跳动' if chinese else 'ByteDance'}</span></a> /
      <a class="company" href="https://www.alibabacloud.com/"><img src="/img/company/alibaba-cloud-icon.png" alt="" /><span>{'阿里云' if chinese else 'Alibaba Cloud'}</span></a> /
      <a class="company" href="https://www.intel.com/"><img src="/img/company/intel-icon.svg" alt="" /><span>Intel</span></a>
      {c['experience']}
    </p>
    <p>{c['focus']}</p>
    <p>{c['approach']}</p>
    <p class="intro-links"><a href="{GITHUB}">GitHub ↗</a><a href="https://ifdian.net/a/itool/plan">{c['support']} ↗</a></p>
  </section>
  <section class="block" id="work" aria-labelledby="projects">
    <h2 id="projects">{c['work']}</h2><p class="section-intro">{c['work_intro']}</p>
    <div class="project-list">
{projects}
    </div>
  </section>
  <section class="block" aria-labelledby="other-title"><h2 id="other-title">{c['other']}</h2><ul class="other-projects">
{others}
    </ul></section>
  <section class="block" id="stack" aria-labelledby="stack-title"><h2 id="stack-title">{c['stack']}</h2><p>{c['stack_text']}</p></section>
  <section class="block" aria-labelledby="now-title"><h2 id="now-title">{c['now']}</h2><p>{c['now_text']}</p></section>
  <hr />
  <section class="block" id="find-me" aria-labelledby="contact-title"><h2 id="contact-title">{c['contact']}</h2><p>{c['contact_text']}</p><p><a href="{GITHUB}">github.com/LiuTianjie</a></p><div class="qr-list"><figure><img src="/img/wechat-qr.png" alt="{c['wechat_alt']}" width="132" height="132" loading="lazy" /><figcaption>{c['wechat']}</figcaption></figure><figure><img src="/img/github-qr.png" alt="{c['github_alt']}" width="132" height="132" loading="lazy" /><figcaption>GitHub</figcaption></figure></div></section>
  <footer><p>© 2026 Liu Tao · <a href="{GITHUB}">@LiuTianjie</a></p></footer>
</main>
</body>
</html>
'''

if __name__=='__main__':
 for c in COPY.values():
  (ROOT/c['file']).write_text(render(c),encoding='utf-8')
  print('Built '+c['file'])
