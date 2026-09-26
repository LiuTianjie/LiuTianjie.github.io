"""Generate the two static portfolio pages. No runtime or third-party dependencies."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
GITHUB = 'https://github.com/LiuTianjie'
BASE = 'https://liutianjie.github.io'

COPY = {
'en': {
 'lang':'en', 'file':'index.html', 'alternate':'/zh.html', 'switch':'中文', 'skip':'Skip to content',
 'title':'Liu Tao — Practical tools for AI workflows',
 'description':'Liu Tao builds native apps, remote workspaces, and self-hosted tools for AI workflows. Explore LinkShell, StupidMirror, Luma, and more.',
 'nav':['Work','About','GitHub'], 'eyebrow':'Liu Tao · Builder & engineer',
 'headline':'AI tools for<br /><em>real work.</em>',
 'intro':'I build native apps, remote workspaces, and self-hosted tools that bring AI into everyday work. You might know me as Nickname4th.',
 'explore':'Explore the work', 'follow':'Follow on GitHub', 'bench':'On my workbench', 'bench_tags':['Native apps','AI workflows','Self-hosted'],
 'bench_desc':['Work from anywhere','Give agents a real device','Deploy on your own servers'],
 'selection':'01 / Selected work', 'work_title':'Built to be used.', 'work_desc':'Three starting points. Each solves a problem I have met in my own work.',
 'link_title':'Your workspace,<br />away from your desk.',
 'link_desc':'Continue a local terminal or coding-agent task from your phone or browser. Your tools and processes stay on your computer.',
 'link_platform':'iOS · Android · Browser', 'link_action':'Try LinkShell', 'source':'Source & docs', 'demo':'Watch a demo',
 'copy':'Copy', 'copied':'Copied', 'copyfail':'Select the command to copy it.', 'install':'Install the CLI on your computer',
 'link_caption':'LinkShell: terminal and session switching in the mobile app.',
 'mirror_title':'A real device.<br />An agent that can use it.',
 'mirror_desc':'Mirror iOS and Android devices on your Mac. A local MCP server lets an agent observe the screen, find a target, act, and check the result.',
 'mirror_platform':'macOS · iOS & Android · MCP', 'mirror_action':'Explore StupidMirror',
 'mirror_note':'Source available · noncommercial license', 'mirror_caption':'StupidMirror running on macOS with a connected iPhone.',
 'luma_title':'Your servers.<br />One deployment workflow.',
 'luma_desc':'Describe a service, choose where it runs, and deploy through a self-hosted control plane. Nomad schedules containers; Luma brings the workflow together.',
 'luma_platform':'Self-hosted · Nomad · Containers', 'luma_action':'Get started with Luma', 'luma_caption':'An example manifest. Deployment requires a configured Luma manager.',
 'more_title':'Also on the bench', 'more_desc':'Smaller tools, different surfaces, the same attention to the work.',
 'other':[
  ('Saylane','On-device dictation, Pinyin, and translation in your macOS text field.','macOS','https://github.com/LiuTianjie/Saylane','/img/projects/saylane-icon.png'),
  ('pura','A shared Android device workspace for team reviews and annotated feedback.','Team tools','https://github.com/LiuTianjie/pura','/img/projects/pura-icon.png'),
  ('gitea-review-agent','Self-hosted AI code reviews and alert analysis for Gitea.','Developer tools','https://github.com/LiuTianjie/gitea-review-agent','')],
 'notes_label':'02 / Inside the tools', 'notes_title':'The decisions behind the interface.',
 'notes':[
  ('LinkShell','From a terminal to an agent workspace','How the terminal and structured agent adapters fit together.','https://github.com/LiuTianjie/LinkShell#agent-workspace'),
  ('StupidMirror','Observe. Act. Verify.','A local MCP interface for working with real mobile devices.','https://github.com/LiuTianjie/StupidMirror#connect-an-ai-agent'),
  ('Luma','Placement and exposure','Separating where a service runs from how traffic reaches it.','https://github.com/LiuTianjie/luma#placement-and-exposure')],
 'read':'Read the project notes', 'about_label':'03 / The person behind the tools', 'about_title':'Hi, I’m Liu Tao.',
 'about_p1':'I work across frontend engineering, product experience, and AI education. Previously, I was a software / senior frontend engineer at ByteDance, Alibaba Cloud, and Intel.',
 'about_p2':'I like taking a recurring frustration, building a tool around it, and refining it through use. The interesting part is the whole path: interface, system behavior, installation, and the first useful result.',
 'about_p3':'Alongside these developer tools, I build in AI education. That work keeps me thinking about how technology can help people learn, create, and get unstuck.',
 'elsewhere':'More of my work', 'past':[('BrowserDisplay','https://liutianjie.github.io/BrowserDisplay/'),('1Doc','https://github.com/LiuTianjie/1Doc'),('Pencil Box','https://gaojiua.com/'),('iTool','https://itool.tech')],
 'contact_title':'Try something. Tell me what happens.', 'contact_desc':'Found a bug, have an idea, or want to contribute? An issue in the relevant repository is the best place to start.',
 'contact_github':'Find me on GitHub', 'wechat':'Connect on WeChat', 'wechat_alt':'WeChat contact QR code for Liu Tao', 'support':'Support my work',
 'footer':'Independent tools, made with care.', 'top':'Back to top', 'notfound':'This page has moved or does not exist.', 'home':'Return to the work',
},
'zh': {
 'lang':'zh-CN', 'file':'zh.html', 'alternate':'/', 'switch':'EN', 'skip':'跳到正文',
 'title':'刘涛 Liu Tao — 让 AI 进入真实工作流',
 'description':'刘涛的个人作品：原生应用、远程工作台和自托管工具。了解 LinkShell、StupidMirror、Luma，以及更多面向真实工作流的 AI 工具。',
 'nav':['作品','关于','GitHub'], 'eyebrow':'刘涛 Liu Tao · 产品开发者',
 'headline':'让 AI，进入<br /><em>真实的工作。</em>',
 'intro':'我构建原生应用、远程工作台和自托管工具，让 AI 融入每天的工作。你也可能通过 Nickname4th 这个名字认识我。',
 'explore':'看看我的作品', 'follow':'在 GitHub 关注', 'bench':'正在打磨的作品', 'bench_tags':['原生应用','AI 工作流','自托管'],
 'bench_desc':['离开电脑，继续工作','让 Agent 操作真实设备','把服务部署到自己的机器'],
 'selection':'01 / 代表作品', 'work_title':'从实际使用出发。', 'work_desc':'三个了解我的起点，都来自我在真实工作中遇到的问题。',
 'link_title':'离开电脑，<br />工作仍在手边。',
 'link_desc':'在手机或浏览器中继续本地终端与编程 Agent 的任务。工具和进程留在电脑上，你可以换一个地方继续工作。',
 'link_platform':'iOS · Android · 浏览器', 'link_action':'体验 LinkShell', 'source':'源码与文档', 'demo':'观看演示',
 'copy':'复制', 'copied':'已复制', 'copyfail':'请选择命令文字进行复制。', 'install':'在电脑上安装 CLI',
 'link_caption':'LinkShell 手机端：终端操作与会话切换。',
 'mirror_title':'真实的手机，<br />Agent 也能操作。',
 'mirror_desc':'在 Mac 上镜像 iOS 与 Android 真机，通过本地 MCP Server，让 Agent 观察画面、定位目标、执行操作并检查结果。',
 'mirror_platform':'macOS · iOS 与 Android · MCP', 'mirror_action':'了解 StupidMirror',
 'mirror_note':'源码可用 · 非商业许可证', 'mirror_caption':'StupidMirror 在 macOS 上显示已连接的 iPhone。',
 'luma_title':'自己的服务器，<br />统一的部署方式。',
 'luma_desc':'描述服务，选择运行位置，再通过自托管控制面完成部署。Nomad 负责调度容器，Luma 将日常部署流程连接起来。',
 'luma_platform':'自托管 · Nomad · 容器', 'luma_action':'开始使用 Luma', 'luma_caption':'部署清单示例，实际部署需要已配置的 Luma Manager。',
 'more_title':'工作台上的其他作品', 'more_desc':'不同的使用场景，同样围绕具体的问题。',
 'other':[
  ('Saylane','在 macOS 当前输入框里，使用端侧听写、拼音与翻译。','macOS','https://github.com/LiuTianjie/Saylane','/img/projects/saylane-icon.png'),
  ('pura','团队共享 Android 真机，一起评审并记录带标注的反馈。','团队工具','https://github.com/LiuTianjie/pura','/img/projects/pura-icon.png'),
  ('gitea-review-agent','为 Gitea 自托管 AI 代码审查与告警分析。','开发工具','https://github.com/LiuTianjie/gitea-review-agent','')],
 'notes_label':'02 / 走进实现', 'notes_title':'界面背后的工程选择。',
 'notes':[
  ('LinkShell','从终端到 Agent 工作台','终端与结构化 Agent 适配器如何配合。','https://github.com/LiuTianjie/LinkShell/blob/main/README_CN.md#agent-workspace'),
  ('StupidMirror','观察、操作，再验证','通过本地 MCP 与真实移动设备协作。','https://github.com/LiuTianjie/StupidMirror/blob/main/README.zh-CN.md#连接-ai-agent'),
  ('Luma','调度位置与访问入口','分别描述服务运行在哪里，以及流量如何到达。','https://github.com/LiuTianjie/luma/blob/main/README.zh-CN.md#调度与入口')],
 'read':'阅读项目说明', 'about_label':'03 / 作品背后的人', 'about_title':'你好，我是刘涛。',
 'about_p1':'我的背景是前端工程、产品体验与 AI 教育，曾在字节跳动、阿里云和 Intel 从事软件与高级前端工程工作。',
 'about_p2':'我喜欢从反复遇到的问题出发，做成工具，再通过实际使用把它打磨好。界面、系统行为、安装体验，以及用户完成的第一件有用的事，都属于产品的一部分。',
 'about_p3':'除了这些开发工具，我也在 AI 教育领域做产品。这让我持续思考：技术如何帮助人们学习、创造，以及跨过眼前的一道障碍。',
 'elsewhere':'更多作品', 'past':[('BrowserDisplay','https://liutianjie.github.io/BrowserDisplay/'),('1Doc','https://github.com/LiuTianjie/1Doc'),('笔袋','https://gaojiua.com/'),('iTool','https://itool.tech')],
 'contact_title':'试试看，告诉我你的体验。', 'contact_desc':'发现问题、有新想法，或希望参与贡献？欢迎在对应仓库提 Issue，让讨论围绕实际使用展开。',
 'contact_github':'在 GitHub 找到我', 'wechat':'通过微信联系', 'wechat_alt':'刘涛的微信联系二维码', 'support':'支持我的工作',
 'footer':'认真做一些有用的工具。', 'top':'回到顶部', 'notfound':'这个页面已经移动，或暂时不存在。', 'home':'返回作品主页',
}}

def link(url, label, cls='text-link'):
    return f'<a class="{cls}" href="{escape(url, quote=True)}">{label}<span aria-hidden="true"> ↗</span></a>'

def render(c):
    canonical=BASE+('/zh.html' if c['lang']=='zh-CN' else '/')
    bench=''.join(f'<a class="bench-row" href="#{id}"><img src="{img}" width="44" height="44" alt="" /><span><strong>{name}</strong><small>{desc}</small></span><span class="arrow" aria-hidden="true">↗</span></a>' for id,name,img,desc in zip(['linkshell','stupidmirror','luma'],['LinkShell','StupidMirror','Luma'],['/img/linkshell-icon.png','/img/projects/stupidmirror-icon.webp','/img/projects/luma-icon.png'],c['bench_desc']))
    more=''.join(f'<a class="project-row" href="{url}">'+(f'<img src="{img}" alt="" width="44" height="44" loading="lazy" />' if img else '<span class="code-mark" aria-hidden="true">&lt;/&gt;</span>')+f'<span><strong>{name}</strong><span>{desc}</span></span><small>{category}</small><span aria-hidden="true">↗</span></a>' for name,desc,category,url,img in c['other'])
    notes=''.join(f'<a class="note-row" href="{url}"><span class="note-origin">{name}</span><span><strong>{title}</strong><span>{desc}</span></span><span aria-hidden="true">↗</span></a>' for name,title,desc,url in c['notes'])
    past=''.join(link(url,name) for name,url in c['past'])
    return f'''<!doctype html>
<html lang="{c['lang']}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#f7f7f2" />
  <meta name="description" content="{c['description']}" />
  <meta name="author" content="Liu Tao" />
  <meta property="og:title" content="{c['title']}" />
  <meta property="og:description" content="{c['description']}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{BASE}/img/liu-tao-avatar.png" />
  <meta property="og:image:alt" content="Liu Tao's GitHub avatar" />
  <meta name="twitter:card" content="summary" />
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="en" href="{BASE}/" />
  <link rel="alternate" hreflang="zh-CN" href="{BASE}/zh.html" />
  <link rel="alternate" hreflang="x-default" href="{BASE}/" />
  <link rel="icon" href="/img/favicon.svg" type="image/svg+xml" />
  <link rel="preload" href="/img/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/css/main.css?v=20260926" />
  <script defer src="/js/main.js?v=20260926"></script>
  <title>{c['title']}</title>
</head>
<body id="top">
<a class="skip-link" href="#main">{c['skip']}</a>
<div class="page">
<header class="site-header">
  <a class="wordmark" href="{'/zh.html' if c['lang']=='zh-CN' else '/'}" aria-label="Liu Tao — home"><span class="monogram" aria-hidden="true">lt.</span><span>Liu Tao<small>Nickname4th</small></span></a>
  <nav aria-label="{'主导航' if c['lang']=='zh-CN' else 'Main navigation'}"><a href="#work">{c['nav'][0]}</a><a href="#about">{c['nav'][1]}</a><a href="{GITHUB}">GitHub<span aria-hidden="true"> ↗</span></a><a class="language" href="{c['alternate']}" lang="{'en' if c['lang']=='zh-CN' else 'zh-CN'}">{c['switch']}</a></nav>
</header>
<main id="main">
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-copy"><p class="eyebrow">{c['eyebrow']}</p><h1 id="hero-title">{c['headline']}</h1><p class="intro">{c['intro']}</p><div class="hero-links"><a class="button" href="#work">{c['explore']} <span aria-hidden="true">↓</span></a>{link(GITHUB,c['follow'])}</div></div>
    <aside class="workbench" aria-label="{c['bench']}"><div class="bench-label"><span class="status-dot" aria-hidden="true"></span>{c['bench']}</div>{bench}<div class="bench-footer">{''.join('<span>'+tag+'</span>' for tag in c['bench_tags'])}</div></aside>
  </section>
  <section id="work" class="section" aria-labelledby="work-title">
    <header class="section-header"><p class="eyebrow">{c['selection']}</p><h2 id="work-title">{c['work_title']}</h2><p>{c['work_desc']}</p></header>
    <article class="featured linkshell" id="linkshell" aria-labelledby="linkshell-title">
      <div class="project-copy"><div class="project-name"><img src="/img/linkshell-icon.png" alt="" width="42" height="42" /><span>LinkShell</span><span class="project-number">01</span></div><h3 id="linkshell-title">{c['link_title']}</h3><p>{c['link_desc']}</p><p class="platform">{c['link_platform']}</p><div class="project-links">{link(BASE+'/LinkShell/',c['link_action'],'text-link primary-link')}{link(GITHUB+'/LinkShell',c['source'])}{link('https://github.com/user-attachments/assets/cc09d3a7-239c-4d5c-a2a7-76f64d4af070',c['demo'])}</div><div class="install"><label for="install-command">{c['install']}</label><div class="command"><code id="install-command">npm install -g linkshell-cli</code><button type="button" data-copy="npm install -g linkshell-cli" data-copied="{c['copied']}" data-error="{c['copyfail']}" aria-label="{c['copy']} npm install command">{c['copy']}</button></div><span class="copy-status" aria-live="polite"></span></div></div>
      <figure class="project-visual phone-stage"><div class="phones"><img src="/img/projects/linkshell-terminal.png" width="1096" height="2140" alt="{'LinkShell 手机终端' if c['lang']=='zh-CN' else 'LinkShell mobile terminal'}" loading="lazy" /><img src="/img/projects/linkshell-sessions.png" width="1096" height="2140" alt="{'LinkShell 会话切换' if c['lang']=='zh-CN' else 'LinkShell session switcher'}" loading="lazy" /></div><figcaption>{c['link_caption']}</figcaption></figure>
    </article>
    <article class="featured mirror" id="stupidmirror" aria-labelledby="mirror-title">
      <div class="project-copy"><div class="project-name"><img src="/img/projects/stupidmirror-icon.webp" alt="" width="42" height="42" /><span>StupidMirror</span><span class="project-number">02</span></div><h3 id="mirror-title">{c['mirror_title']}</h3><p>{c['mirror_desc']}</p><p class="platform">{c['mirror_platform']}</p><div class="project-links">{link(BASE+'/StupidMirror/',c['mirror_action'],'text-link primary-link')}{link(GITHUB+'/StupidMirror',c['source'])}</div><p class="license-note">{c['mirror_note']}</p></div>
      <figure class="project-visual mirror-stage"><img src="/img/projects/stupidmirror.webp" width="1900" height="1585" loading="lazy" alt="{c['mirror_caption']}" /><figcaption>{c['mirror_caption']}</figcaption></figure>
    </article>
    <article class="featured luma" id="luma" aria-labelledby="luma-title">
      <div class="project-copy"><div class="project-name"><img src="/img/projects/luma-icon.png" alt="" width="42" height="42" /><span>Luma</span><span class="project-number">03</span></div><h3 id="luma-title">{c['luma_title']}</h3><p>{c['luma_desc']}</p><p class="platform">{c['luma_platform']}</p><div class="project-links">{link(BASE+'/luma/',c['luma_action'],'text-link primary-link')}{link(GITHUB+'/luma',c['source'])}</div></div>
      <figure class="project-visual manifest-stage"><div class="manifest"><div class="manifest-bar"><span>status.yaml</span><span>YAML</span></div><pre><code><span class="code-key">name:</span> status
<span class="code-key">image:</span> traefik/whoami:v1.10.3
<span class="code-key">region:</span> cn
<span class="code-key">exposure:</span> cn-edge
<span class="code-key">domain:</span> status.example.com
<span class="code-key">port:</span> 80</code></pre><div class="manifest-command"><span aria-hidden="true">$ </span>luma deploy status.yaml</div></div><figcaption>{c['luma_caption']}</figcaption></figure>
    </article>
    <div class="more-work"><h3>{c['more_title']}</h3><p>{c['more_desc']}</p><div class="project-rows">{more}</div></div>
  </section>
  <section class="section notes" aria-labelledby="notes-title"><header class="section-header"><p class="eyebrow">{c['notes_label']}</p><h2 id="notes-title">{c['notes_title']}</h2></header><div aria-label="{c['read']}">{notes}</div></section>
  <section id="about" class="section about" aria-labelledby="about-title"><div><p class="eyebrow">{c['about_label']}</p><h2 id="about-title">{c['about_title']}</h2><img class="portrait" src="/img/liu-tao-avatar.png" alt="Liu Tao" width="120" height="120" loading="lazy" /><p class="handle">@LiuTianjie / Nickname4th</p></div><div class="about-copy"><p>{c['about_p1']}</p><p>{c['about_p2']}</p><p>{c['about_p3']}</p><p class="small-label">{c['elsewhere']}</p><div class="past-projects">{past}</div></div></section>
  <section class="contact" id="contact" aria-labelledby="contact-title"><div><h2 id="contact-title">{c['contact_title']}</h2><p>{c['contact_desc']}</p></div><div class="contact-links">{link(GITHUB,c['contact_github'],'text-link primary-link')}{link('https://ifdian.net/a/itool/plan',c['support'])}<details class="wechat"><summary>{c['wechat']}</summary><img src="/img/wechat-qr.png" alt="{c['wechat_alt']}" width="180" height="180" loading="lazy" /></details></div></section>
</main>
<footer><span>© 2026 Liu Tao <span class="footer-note">· {c['footer']}</span></span><a href="#top">{c['top']} ↑</a></footer>
</div>
</body>
</html>
'''

if __name__ == '__main__':
    for locale, copy in COPY.items():
        (ROOT/copy['file']).write_text(render(copy),encoding='utf-8')
        print(f'Built {copy["file"]}')
