# STC 论坛自动签到脚本
www.STCAIMCU.com 自动签到    

## 简介
该项目利用 Github Actions 实现 STC 国芯论坛的自动化每日签到

## 使用方法
### Fork 本仓库
点击右上角的 Fork 按钮将本仓库 Fork 到你的账号下

<p align="center">
<img src="/img/img_01.png" width="500">      
</p>

### 配置 Secrets
进入 www.STCAIMCU.com 登录账号，按 F12 进入 `网络` 选项卡，刷新页面，找到请求 `www.stcaimcu.com`，复制其中的 Cookie

<p align="center">  
<img src="/img/img_02.png" width="500">            
</p>

进入你 Fork 到你账号下的仓库，在 **`Settings -> Secrets and variables -> Actions -> Repository secrets`** 点击 **`New repository secret`** 创建 Secret:  

- `Name`: `STCAIMCU_COOKIES`
- `Secret`: 刚刚复制得到的全部 Cookie

### 启用 Actions 并手动触发工作流
在你 Fork 到你账号下的仓库中找到 Actions 选项卡，进入，点击 **`I understand my workflows, go ahead and enable them`** 启用 Actions

<p align="center">
<img src="/img/img_03.png" width="500">              
</p>

进入工作流 `Auto Check-in` 启用此工作流，然后手动触发工作流查看效果

<p align="center">
<img src="/img/img_04.png" width="500">
<img src="/img/img_05.png" width="500">      
</p>

### 修改自动运行时间
你可以使用 [Cron 表达式生成器](https://calctools.online/zh/time/cron)生成 Cron 表达式，编辑 [**`.github/workflows/check-in.yml`** 中的第5行](https://github.com/klxf/stc-auto-check-in/blob/5510b116f27631cec57cfdc81206febe78e3d0ef/.github/workflows/check-in.yml#L5)修改自动签到时间

默认为每天的 16:05(UTC)[^1] 自动运行工作流

## 本地部署
在写了在写了


[^1]: 北京时间：00:05(UTC+8)
