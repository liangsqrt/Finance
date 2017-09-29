#_*_coding:utf-8_*_
import re


this_div='''

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    

    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="renderer" content="webkit">
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
    <meta name="mobile-agent" content="format=html5; url=http://m.guba.eastmoney.com/article/600256419">
    <link rel="canonical" href="http://guba.eastmoney.com/news,tzzh,600256419.html" />

    <title>用户6230094050021150创建了实盘组合_投资组合(tzzh)股吧_东方财富网股吧</title>
    <meta content="用户6230094050021150创建了实盘组合_投资组合(tzzh)_投资组合股吧_tzzh股吧_股吧_东方财富网股吧_投资组合吧最新行情_股吧投资指南_投资组合吧k线图分析_股吧行情分析" name="keywords">
    <meta content="用户6230094050021150创建了实盘组合_投资组合_股吧_东方财富网股吧_人气财经股吧_guba.eastmoney.com" name="description">
    
    <link rel="stylesheet" href="//gbfek.dfcfw.com/gubav5/css/news_c_50d0a634c1.css" />
    <base target="_blank" />
    
    <script>
        var barcode = "tzzh";
        var stockcode = "tzzh1";
        var code = "tzzh";
        var topicid="600256419";
        var zwuser = "缘来是你29011";
        var guba_type = "10";
        var dis_wzc = false;
        var stockname = "投资组合";
        var plqx=0;
    
        var OuterCode = "tzzh";
        var Category="205";
        var Division="2";
        var Market="-1";
        var Type="-1";
        var QuoteCode="";
        var BarType="3";
        var CodeWithMarket = "tzzh";
    var qq_code = "";var qq_code2 = "";
        var topictype = 9;
    </script>
</head>
<body class="hlbody">
    
<style>
    #topnav li .red_point_jj {
        position: absolute;
        top: -3px;
        left: 30px;
        background-image: url(http://gbfek.dfcfw.com/gubav5/images/header_bg.png);
        background-position: -25px 0;
        width: 6px;
        height: 6px;
        margin: 0 auto;
    }

    #topnav li {
        display: inline-block;
        padding: 0 6px;
        *display: inline;
        *zoom: 1;
        position: relative;
        height: 30px;
    }

    .guba_topic .topics {
        display: none;
    }

    .guba_topic ul li {
        display: block;
        background-color: #08417f;
        width: 61px;
        height: 33px;
        margin-top: 2px;
        line-height: 33px;
        text-align: center;
    }

    .guba_topic:hover ul {
        display: block;
        position: absolute;
        top: 25px;
        left: -13px;
    }
</style>
<div id="header">
    <!-- 微信分享img -->
    <img id="weixin-share" src="http://cmsjs.eastmoney.com/common/weixin-share.png" style="position: absolute; width: 0; height: 0; left: -1000px; z-index: -1;">
    <div class="gbbody" id="headergbbody">
        <ul id="topnav">
            <li><a href="http://www.eastmoney.com/" target="_blank" tracker-eventcode="iguba_topbar_href_dfcfw">东方财富网</a></li>
            |
			<li><a href="http://fund.eastmoney.com/" target="_blank" tracker-eventcode="iguba_topbar_href_ttjjw">天天基金网</a></li>
            |
			<li><a href="http://guba.eastmoney.com/" target="_blank" tracker-eventcode="iguba_topbar_href_gbsy">股吧首页</a></li>
            |
			<li><a href="//guba.eastmoney.com/jj.html" tracker-eventcode="iguba_topbar_href_jjbsy">基金吧</a></li>
            |
			<!-- <li><a href="http://iguba.eastmoney.com/" target="_blank" tracker-eventcode="iguba_topbar_href_wdgb">我的股吧</a></li> -->
            <!-- <li><a href="http://guba.eastmoney.com/remenba.aspx?type=1" target="_blank">热门吧</a></li> -->
            <li><a href="http://guba.eastmoney.com/ft_list.aspx" target="_blank" tracker-eventcode="iguba_topbar_href_gbft">股吧访谈</a></li>
            |
            
            
            <li class="guba_topic"><a href="http://gubatopic.eastmoney.com/" target="_blank">股吧话题</a><i class="red_point"></i></li>
            
			|
			<li><a href="http://guba.eastmoney.com/qa/qa_list.aspx" target="_blank" tracker-eventcode="iguba_topbar_href_wdm">问董秘</a></li>
            |
			<li><a href="http://cp.eastmoney.com//cp20161013/index.html?tz=webtg_gubaapp_act_top1_06_01_01_1&webtg_gubaapp_act_top1_06_01_02_1" target="_blank" tracker-eventcode="iguba_topbar_href_sjb">股吧手机版</a></li>
        </ul>
        <!-- 功能废弃2017-06-08 -->
        <!-- <form method="GET" action="" id="topnavsearch" target="_blank">
			<input type="text" name="" id="topnavskey" placeholder="搜索 股票/讨论/用户" autocomplete="off" /><input type="submit" value=" " id="topnavsubmit" title="点击开始搜索" tracker-eventcode="iguba_topbar_search_topbarS"/>
			<div id="topnavsearchre">
				<ul ></ul>
			</div>
		</form> -->
        <ul id="topnavper">
            <li class="topbarhaslogin" id="topbarloginuserdiv" style="display: none;">
                <span class="headerusername tnavsel">
                    <em class="userhead"></em>
                    <span class="username"></span>
                    <em class="tnavselic"></em>
                    <div class="topnavdown">
                        <!-- <div class="topnavdownt">设置<em class="tnavselid"></em></div> -->
                        <ul class="topnavdownul">
                            <li><a href="https://passport.eastmoney.com/pub/basicinfo" target="_blank">个人设置</a></li>
                            <li><a href="https://passport.eastmoney.com/pub/changepassword" target="_blank">修改密码</a></li>
                            <li><a href="//iguba.eastmoney.com/setting/privacy" target="_blank">隐私设置</a></li>
                            <li><a href="//iguba.eastmoney.com/setting/message" target="_blank">消息设置</a></li>
                            <li><a href="http://v.eastmoney.com" target="_blank">V认证</a></li>
                            <li class="nobg"><a href="javascript:;" target="_self" id="topbarlogoutlink">退出</a></li>
                        </ul>
                    </div>
                </span>
            </li>
            <li class="topbarhaslogin" style="display: none;">
                <span class="tnavsel"><a href="//iguba.eastmoney.com/"><em class="top_name">我的股吧</em></a><em class="tnavselic"></em>
                    <div class="topnavdown">
                        <!-- <div class="topnavdownt">设置<em class="tnavselid"></em></div> -->
                        <ul class="topnavdownul">
                            <li><a href="//iguba.eastmoney.com/">我关注的股</a></li>
                            <li><a href="//iguba.eastmoney.com/myfollper">我关注的人</a></li>
                            <li><a href="//iguba.eastmoney.com/myart">我的发言</a></li>
                            <li><a href="//iguba.eastmoney.com/myfav">我的收藏</a></li>
                        </ul>
                    </div>
                </span>
            </li>

            <li class="topbarhaslogin" style="display: none;"><span class="tnavsel"><em class="top_name my_msg">我的消息<i></i></em><em class="tnavselic"></em>
                <div class="topnavdown">
                    <!-- <div class="topnavdownt">消息<em class="tnavselid"></em></div> -->
                    <ul class="topnavdownul topnavdownulmsgul">
                        <li><a href="//iguba.eastmoney.com/replyme">&nbsp;&nbsp;查看新回复<em></em></a></li>
                        <li><a href="//iguba.eastmoney.com/atmereply">&nbsp;&nbsp;查看新@我的<em></em></a></li>
                        <li><a href="//iguba.eastmoney.com/myfans">&nbsp;&nbsp;查看新粉丝<em></em></a></li>
                        <li><a href="javascript:;" target="_self" class="alarm" data-type="1">&nbsp;&nbsp;股价提醒<em></em></a></li>
                        <li><a href="javascript:;" target="_self" class="alarm" data-type="2">&nbsp;&nbsp;公告提醒<em></em></a></li>
                        <li><a href="javascript:;" target="_self" class="alarm" data-type="3">&nbsp;&nbsp;研报提醒<em></em></a></li>
                        <li class="nobg"><a href="javascript:;" class="alarm" data-type="4" target="_self">&nbsp;&nbsp;数据提醒<em></em></a></li>
                    </ul>
                </div>
            </span>
            </li>
            <li class="topbarlogin tnavselloginfix">您好，欢迎来股吧！  </li>
            <li class="topbarlogin tnavsellogin"><a id="header_btn_login" href="javascript:;" target="_self" tracker-eventcode="iguba_topbar_log_in"><strong>登录/注册</strong></a>
                <script>
                    var url = "https://passport.eastmoney.com/pub/login?backurl=" + encodeURIComponent(window.location.href);
                    document.getElementById("header_btn_login").href = url;
                </script>
            </li>
        </ul>
    </div>
</div>
<script>
    window.shimingOption = 2;
</script>

    <div id="header_ad" class="gbbody">
        <div class="dh10"></div>
        <iframe width="980" height="60" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" src="http://same.eastmoney.com/s?z=eastmoney&c=1048&op=1"></iframe>
    </div>
    <div id="headerban" class="gbbody">
	<div id="headerbanlogo"><a href="/"><img src="http://guba.eastmoney.com/images/gubahlogo.png" width="252" height="52" alt="股吧" /></a></div>
	<div id="gbhsearch">
		<form id="gbhscform">
			<ul id="gbhsctab">
				<li class="on">搜股吧</li>
				<li>搜内容</li>
				<li>搜作者</li>
				<li>搜话题</li>
			</ul>
			<input type="text" name="" id="gbhsckey" />
			<input type="text" name="" id="gbhsckey2" style="width: 287px;height: 25px;border: 1px solid #CADFF6;border-top: 0; float: left;padding:0 4px;color:#6D6D6D;line-height: 25px;display:none;" />
			<input type="submit" value="股吧搜索" id="gbhscsbm" />
		</form>
	</div>
	<div id="gbhri">
		热门：<a href="/list,601011.html">宝泰隆吧</a> <a href="/list,000725.html">京东方A吧</a> <a href="/list,600760.html">中航黑豹吧</a> 
	</div>
</div>

    <div id="stockheader" class="gbbody">
        <span id="stockif">
            <span id="stockname" data-popstock="tzzh" data-poptype="1"><a href="/list,tzzh.html">投资组合吧</a></span>
        </span>
        <span id="header_stock_btns"></span>
        <div id="zjfw" class="zjfw">
            <ul>
                <li class="zjfwdb">最近访问：</li>
                <li><span id="baHistory"></span></li>
            </ul>
        </div>
    </div>
    <div class="zwheadbline gbbody">
        <div class="zwheadblineb"></div>
    </div>
    <div class="gbbody">
        <div id="mainbody">
            
            <div class="zwheadpager">
                <div class="zwhpager"></div>
                <div class="zwhpagerr"><a href="list,tzzh.html">返回投资组合吧&gt;&gt;</a></div>
            </div>
            <div id="zwmbti">
                <ul id="head_topic" class="head_topic">
                    <li class="topic">
                        <a style="color: red; !important" href="http://js1.eastmoney.com/tg.aspx?ID=3979" target="_blank">[头条]白酒股领涨
                        </a>
                    </li>
                    <li class="topic">
                        <ul><li><a href="http://acttg.eastmoney.com/pub/web_nr_gbzwy_ttz_01_01_01_0" >好文章，能赚钱！</a></li></ul>
                    </li>
                </ul>

                <div id="zwmbtilr"></div>
            </div>
            
            <div id="zwcontent" >

                <div id="zwcontt">
                    <div id="zwconttphoto"><a href="http://iguba.eastmoney.com/6230094050021150" data-poptype="2" data-popper="6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/50" width="50" height="50" class="userphoto" /></a></div>
                    <div id="zwconttb">
                        <div id="zwconttbn">
                            <strong><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></strong>  <span class="influence" data-uid="6230094050021150"></span>
                        </div>
                        <div class="zwfbtime">发表于 2017-02-04 15:38:04 股吧网页版</div>

                    </div>
                    <div id="zwconttbtns">
                        <a href="http://iguba.eastmoney.com/secr.aspx?code=tzzh&id=600256419" style="display: none;" id="dongmilink" class="graylink">董秘直通车</a>&ensp;<a href="javascript:;" target="_self" id="jubaolink" class="graylink">举报</a>
                    </div>
                </div>

                
                <div class="zwcontentmain">

                    <div id="zwconttbt">
                        用户6230094050021150创建了实盘组合
                        
                    </div>
                    
                    <div id="zwconbody">
                        <div class="stockcodec">
                            
                            组合 id:200176280 
                        </div>
                        
                    </div>

                </div>
                

                <div class="zwconbtns clearfix">
                    <div class="zwconbtnsi" id="zwconbtnsi_pl" onclick="try{gudong.stat(3,null);}catch (e){};">
                        <div class="zwconbtnsii"></div>
                        <a href="javascript:;" target="_self">我要评论</a>
                    </div>
                    <div class="zwconbtnsi" id="zwconbtnsi_zf" onclick="try{gudong.stat(4,null);}catch (e){};">
                        <div class="zwconbtnsii"></div>
                        <a href="javascript:;" target="_self">转发(<span id="zfnums" class="red">3</span>)</a>
                    </div>
                    <div class="zwconbtnsi" id="zwconbtnsi_z">
                        <div class="zwconbtnsii"></div>
                        <span id="zwpraise"><a href="javascript:;" target="_self">赞</a></span>
                    </div>
                    <div class="zwconbtnsi" id="zwconbtnsi_sc">
                        <div class="zwconbtnsii"></div>
                        <span id="zwconbtsc"><a href="javascript:;" target="_self">收藏本帖</a></span>
                    </div>
                    <div class="zwconbtnsi" id="zwconbtnsi_fx">
                        <div class="zwconbtnsia">
                            <div class="zwconbtnsii"></div>
                            <span id="zwconbtsc"><a href="javascript:;" target="_self">分享</a></span>
                        </div>
                    </div>
                    <div class="zwconbtnsi" id="zwconbtnsi_jb">
                        <div class="zwconbtnsii"></div>
                        <span id="zwpraise"><a href="javascript:;" target="_self">举报本帖</a></span>
                    </div>
                </div>


                <div class="gubamobilegg2014" id="zwcontentbgg" style="display: none; text-align: center;">
                    <ul><li><span class="red"><a href="http://acttg.eastmoney.com/pub/web_kh_gbzwy_dt_01_01_01_1" ><strong>每日一只牛股 两天盈利超15%</strong></a></span>&nbsp;<span class="red"><a href="http://js5.eastmoney.com/tg.aspx?ID=2334 " ><strong>重返3300钱景如何？这样捕捉未来领涨先锋</strong></a></span>&nbsp;<span class="red"><a href="http://acttg.eastmoney.com/pub/web_act_16cgds_hdrk_01_01_23_0" ><strong>必看！这样炒股都赚翻了！</strong></a></span>&nbsp;<span class="red"><a href="http://js1.eastmoney.com/tg.aspx?ID=3744" ><strong>沪指小幅收跌 白酒股领涨</strong></a></span>&nbsp;<span class="red"><a href="http://acttg.eastmoney.com/pub/web_jcb_gbzwy_zwd_01_01_01_1" ><strong>公告现重大利好，10股有望突破大涨！</strong></a></span></li></ul>
                </div>
            
                <div class="clear"></div>

            </div>

            
            <div id="zwcontab">
                <ul>
                    <li class="on"
                        ><a href="news,tzzh,600256419.html" target="_self">全部评论（332）</a></li>
                    
                    <li ><a href="news,tzzh,600256419,6230094050021150.html#storeply" target="_self">只看楼主发言</a></li>
                    
                </ul>
                
                <div id="zwcontabsort">
                    排序<a id="zwzuizaobtn" href="news,tzzh,600256419.html#storeply" target="_self"><span class="on"
                        >最早</span></a><a id="zwzuijinbtn" href="news,tzzh,600256419,d.html#storeply" target="_self"><span >最近</span></a><a href="javascript:;" target="_self"><span id="zwshowzzbtn">最赞</span></a>
                </div>
                
                <div class="clear"></div>
            </div>
            
            <div id="zwlist">
                
                <div class="zwli clearfix" id="zwli8496815108" data-huifuid="8496815108" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8496815108">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-08  21:26:17</div>

                            
                            <div class="zwlitext stockcodec">买的新股显示不出来</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8496815086" data-huifuid="8496815086" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8496815086">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-08  21:26:42</div>

                            
                            <div class="zwlitext stockcodec">买的新股显示不出来</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8496970867" data-huifuid="8496970867" data-huifuuid="2685064973192694">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8496970867">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/2685064973192694"><img src="http://avator.eastmoney.com/qface/2685064973192694/30" data-popper="2685064973192694" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/2685064973192694"  data-popper="2685064973192694" data-poptype="1">股东_陈海宁</a></span> <span class="influence" data-uid="2685064973192694"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-09  08:02:03</div>

                            
                            <div class="zwlitext stockcodec">什么股</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497335443" data-huifuid="8497335443" data-huifuuid="3482005044917204">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497335443">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/3482005044917204"><img src="http://avator.eastmoney.com/qface/3482005044917204/30" data-popper="3482005044917204" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/3482005044917204"  data-popper="3482005044917204" data-poptype="1">陈奕莼</a></span> <span class="influence" data-uid="3482005044917204"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-10  10:16:35</div>

                            
                            <div class="zwlitext stockcodec">你买的什么股</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497448852" data-huifuid="8497448852" data-huifuuid="9561004733523910">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497448852">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/9561004733523910"><img src="http://avator.eastmoney.com/qface/9561004733523910/30" data-popper="9561004733523910" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/9561004733523910"  data-popper="9561004733523910" data-poptype="1">必有师</a></span> <span class="influence" data-uid="9561004733523910"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-10  18:52:58</div>

                            
                            <div class="zwlitext stockcodec">大牛股300263隆华节能下周启动!</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497448748" data-huifuid="8497448748" data-huifuuid="9561004733523910">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497448748">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/9561004733523910"><img src="http://avator.eastmoney.com/qface/9561004733523910/30" data-popper="9561004733523910" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/9561004733523910"  data-popper="9561004733523910" data-poptype="1">必有师</a></span> <span class="influence" data-uid="9561004733523910"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-10  18:53:20</div>

                            
                            <div class="zwlitext stockcodec">大牛股300263隆华节能下周启动!</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497613990" data-huifuid="8497613990" data-huifuuid="6945004914945944">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497613990">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6945004914945944"><img src="http://avator.eastmoney.com/qface/6945004914945944/30" data-popper="6945004914945944" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6945004914945944"  data-popper="6945004914945944" data-poptype="1">一带一路前海</a></span> <span class="influence" data-uid="6945004914945944"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  08:14:37</div>

                            
                            <div class="zwlitext stockcodec">我的股票</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497613995" data-huifuid="8497613995" data-huifuuid="6945004914945944">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497613995">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6945004914945944"><img src="http://avator.eastmoney.com/qface/6945004914945944/30" data-popper="6945004914945944" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6945004914945944"  data-popper="6945004914945944" data-poptype="1">一带一路前海</a></span> <span class="influence" data-uid="6945004914945944"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  08:16:54</div>

                            
                            <div class="zwlitext stockcodec">我的股票</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497641599" data-huifuid="8497641599" data-huifuuid="3673094979999042">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497641599">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/3673094979999042"><img src="http://avator.eastmoney.com/qface/3673094979999042/30" data-popper="3673094979999042" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/3673094979999042"  data-popper="3673094979999042" data-poptype="1">骆小龙</a></span> <span class="influence" data-uid="3673094979999042"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  09:20:59</div>

                            <div class="zwlitalkbox"><div class="zwlitalkboxh"><div class="zwlitalkboxph"><a href="http://iguba.eastmoney.com/6230094050021150" data-poptype="2" data-popper="6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/50" width="30" height="30" class="userphoto" /></a></div><div class="zwlitalkboxuinfo"><div class="zwlitalkboxname zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a>  <span class="influence" data-uid="6230094050021150"></span></div><div class="zwlitalkboxtime">发表于 2017-09-08 21:26:17</div></div></div><div class="zwlitalkboxtext">买的新股显示不出来</div></div>
                            <div class="zwlitext stockcodec">大神买的什么股票，回复下呗</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497666804" data-huifuid="8497666804" data-huifuuid="1547035042766690">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497666804">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/1547035042766690"><img src="http://avator.eastmoney.com/qface/1547035042766690/30" data-popper="1547035042766690" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/1547035042766690"  data-popper="1547035042766690" data-poptype="1">直升机668</a></span> <span class="influence" data-uid="1547035042766690"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  09:59:11</div>

                            
                            <div class="zwlitext stockcodec">盐湖股份 买进了吗？</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497677845" data-huifuid="8497677845" data-huifuuid="3673094979999042">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497677845">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/3673094979999042"><img src="http://avator.eastmoney.com/qface/3673094979999042/30" data-popper="3673094979999042" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/3673094979999042"  data-popper="3673094979999042" data-poptype="1">骆小龙</a></span> <span class="influence" data-uid="3673094979999042"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  10:13:27</div>

                            <div class="zwlitalkbox"><div class="zwlitalkboxh"><div class="zwlitalkboxph"><a href="http://iguba.eastmoney.com/3673094979999042" data-poptype="2" data-popper="3673094979999042"><img src="http://avator.eastmoney.com/qface/3673094979999042/50" width="30" height="30" class="userphoto" /></a></div><div class="zwlitalkboxuinfo"><div class="zwlitalkboxname zwnick"><a href="http://iguba.eastmoney.com/3673094979999042"  data-popper="3673094979999042" data-poptype="1">骆小龙</a>  <span class="influence" data-uid="3673094979999042"></span></div><div class="zwlitalkboxtime">发表于 2017-09-11 09:20:59</div></div></div><div class="zwlitalkboxtext">大神买的什么股票，回复下呗</div></div>
                            <div class="zwlitext stockcodec">说下股票代码</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497710017" data-huifuid="8497710017" data-huifuuid="1547035042766690">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497710017">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/1547035042766690"><img src="http://avator.eastmoney.com/qface/1547035042766690/30" data-popper="1547035042766690" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/1547035042766690"  data-popper="1547035042766690" data-poptype="1">直升机668</a></span> <span class="influence" data-uid="1547035042766690"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  10:53:01</div>

                            
                            <div class="zwlitext stockcodec">看不见发言，也看不见 老师买的票</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8497860147" data-huifuid="8497860147" data-huifuuid="1819124736855070">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8497860147">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/1819124736855070"><img src="http://avator.eastmoney.com/qface/1819124736855070/30" data-popper="1819124736855070" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/1819124736855070"  data-popper="1819124736855070" data-poptype="1">我有一双搂钱手</a></span> <span class="influence" data-uid="1819124736855070"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-11  14:32:51</div>

                            
                            <div class="zwlitext stockcodec">他不是追了盐湖股份了吗</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498595259" data-huifuid="8498595259" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498595259">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  13:50:21</div>

                            
                            <div class="zwlitext stockcodec">明天我要重回前10</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498595634" data-huifuid="8498595634" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498595634">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  13:50:49</div>

                            
                            <div class="zwlitext stockcodec">没有买盐湖,撤单了</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498596178" data-huifuid="8498596178" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498596178">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  13:51:10</div>

                            
                            <div class="zwlitext stockcodec">我买的票都能看到的,但根据大赛规定,买的新股是看不到的</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498597092" data-huifuid="8498597092" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498597092">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  13:53:04</div>

                            
                            <div class="zwlitext stockcodec">盐湖我撤单没买了</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498596781" data-huifuid="8498596781" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498596781">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  13:53:23</div>

                            
                            <div class="zwlitext stockcodec">昨天涨停卖掉了已经,603079</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498601580" data-huifuid="8498601580" data-huifuuid="3530035044910276">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498601580">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/3530035044910276"><img src="http://avator.eastmoney.com/qface/3530035044910276/30" data-popper="3530035044910276" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/3530035044910276"  data-popper="3530035044910276" data-poptype="1">雨林丶</a></span> <span class="influence" data-uid="3530035044910276"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  13:59:13</div>

                            
                            <div class="zwlitext stockcodec">好牛气了，四川双马不知道会几个板，羡慕啊。</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8498630072" data-huifuid="8498630072" data-huifuuid="3530035044910276">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8498630072">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/3530035044910276"><img src="http://avator.eastmoney.com/qface/3530035044910276/30" data-popper="3530035044910276" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/3530035044910276"  data-popper="3530035044910276" data-poptype="1">雨林丶</a></span> <span class="influence" data-uid="3530035044910276"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-12  14:31:18</div>

                            
                            <div class="zwlitext stockcodec">能跟买就好了</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499252871" data-huifuid="8499252871" data-huifuuid="9742094352180166">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499252871">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/9742094352180166"><img src="http://avator.eastmoney.com/qface/9742094352180166/30" data-popper="9742094352180166" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/9742094352180166"  data-popper="9742094352180166" data-poptype="1">潘樱颦</a></span> <span class="influence" data-uid="9742094352180166"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  11:05:13</div>

                            
                            <div class="zwlitext stockcodec">厉害厉害。</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499288700" data-huifuid="8499288700" data-huifuuid="4306015006260850">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499288700">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/4306015006260850"><img src="http://avator.eastmoney.com/qface/4306015006260850/30" data-popper="4306015006260850" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/4306015006260850"  data-popper="4306015006260850" data-poptype="1">高博投资</a></span> <span class="influence" data-uid="4306015006260850"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  11:44:21</div>

                            
                            <div class="zwlitext stockcodec">厉害</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499312942" data-huifuid="8499312942" data-huifuuid="1982513693519920">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499312942">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/1982513693519920"><img src="http://avator.eastmoney.com/qface/1982513693519920/30" data-popper="1982513693519920" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/1982513693519920"  data-popper="1982513693519920" data-poptype="1">期待_上涨</a></span> <span class="influence" data-uid="1982513693519920"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  12:17:55</div>

                            
                            <div class="zwlitext stockcodec">0k</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499349059" data-huifuid="8499349059" data-huifuuid="8161025004360410">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499349059">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/8161025004360410"><img src="http://avator.eastmoney.com/qface/8161025004360410/30" data-popper="8161025004360410" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/8161025004360410"  data-popper="8161025004360410" data-poptype="1">股友vQq1m5</a></span> <span class="influence" data-uid="8161025004360410"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  13:23:50</div>

                            
                            <div class="zwlitext stockcodec">厉害</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499543935" data-huifuid="8499543935" data-huifuuid="8683094506649336">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499543935">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/8683094506649336"><img src="http://avator.eastmoney.com/qface/8683094506649336/30" data-popper="8683094506649336" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/8683094506649336"  data-popper="8683094506649336" data-poptype="1">天天日红</a></span> <span class="influence" data-uid="8683094506649336"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  17:20:10</div>

                            
                            <div class="zwlitext stockcodec">大神 双马从组失败 不知道凶吉！ 现在应该是补涨吧！</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499688722" data-huifuid="8499688722" data-huifuuid="2001513832220782">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499688722">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/2001513832220782"><img src="http://avator.eastmoney.com/qface/2001513832220782/30" data-popper="2001513832220782" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/2001513832220782"  data-popper="2001513832220782" data-poptype="1">guohuaiwei</a></span> <span class="influence" data-uid="2001513832220782"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  21:14:50</div>

                            <div class="zwlitalkbox"><div class="zwlitalkboxh"><div class="zwlitalkboxph"><a href="http://iguba.eastmoney.com/6230094050021150" data-poptype="2" data-popper="6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/50" width="30" height="30" class="userphoto" /></a></div><div class="zwlitalkboxuinfo"><div class="zwlitalkboxname zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a>  <span class="influence" data-uid="6230094050021150"></span></div><div class="zwlitalkboxtime">发表于 2017-09-12 13:53:23</div></div></div><div class="zwlitalkboxtext">昨天涨停卖掉了已经,603079</div></div>
                            <div class="zwlitext stockcodec">赞</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499712779" data-huifuid="8499712779" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499712779">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  21:46:12</div>

                            
                            <div class="zwlitext stockcodec">双马的逻辑看市场怎么看了，也可以说是补涨，也可以说是两个月以后的重组预期</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499712065" data-huifuid="8499712065" data-huifuuid="6230094050021150">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499712065">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/30" data-popper="6230094050021150" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a></span> <span class="influence" data-uid="6230094050021150"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-13  21:46:20</div>

                            
                            <div class="zwlitext stockcodec">明天我要进去前三</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499827467" data-huifuid="8499827467" data-huifuuid="4545094478432688">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499827467">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/4545094478432688"><img src="http://avator.eastmoney.com/qface/4545094478432688/30" data-popper="4545094478432688" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/4545094478432688"  data-popper="4545094478432688" data-poptype="1">白杨哈密尔顿</a></span> <span class="influence" data-uid="4545094478432688"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-14  02:18:52</div>

                            <div class="zwlitalkbox"><div class="zwlitalkboxh"><div class="zwlitalkboxph"><a href="http://iguba.eastmoney.com/6230094050021150" data-poptype="2" data-popper="6230094050021150"><img src="http://avator.eastmoney.com/qface/6230094050021150/50" width="30" height="30" class="userphoto" /></a></div><div class="zwlitalkboxuinfo"><div class="zwlitalkboxname zwnick"><a href="http://iguba.eastmoney.com/6230094050021150"  data-popper="6230094050021150" data-poptype="1">缘来是你29011</a>  <span class="influence" data-uid="6230094050021150"></span></div><div class="zwlitalkboxtime">发表于 2017-09-13 21:46:20</div></div></div><div class="zwlitalkboxtext">明天我要进去前三</div></div>
                            <div class="zwlitext stockcodec">厉害9:35封板了还能25.37卖到</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="zwli clearfix" id="zwli8499921728" data-huifuid="8499921728" data-huifuuid="6737014370031636">
                    <div class="zwjubao"><a href="javascript:;" target="_self" class="graylink" data-replyid="8499921728">举报本回复</a></div>
                    <div class="zwliimg">
                        <a href="http://iguba.eastmoney.com/6737014370031636"><img src="http://avator.eastmoney.com/qface/6737014370031636/30" data-popper="6737014370031636" /></a> 
                    </div>
                    <div class="zwlitx">
                        <div class="zwlitxt">
                            
                            <div class="zwlianame">
                                <span class="zwnick"><a href="http://iguba.eastmoney.com/6737014370031636"  data-popper="6737014370031636" data-poptype="1">前钱难有</a></span> <span class="influence" data-uid="6737014370031636"></span>
                            </div>
                            <div class="zwlitime">发表于 2017-09-14  09:44:58</div>

                            
                            <div class="zwlitext stockcodec">四川双马不卖吗？</div>
                            <div class="zwlitxtbc">
                                <div class="zwlitxb"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <script>var num=2293647;var count=2949659;</script>
                <script>
                    if (typeof (num) == "undefined") {var num=2293580; }var pinglun_num=332;var xgti="";if(typeof (count) != "undefined"){xgti="<span class=\"tc2\"><a href='list,tzzh.html'>相关帖子<span class=\"tc1\">"+count+"</span>条</a></span>";}
                    document.getElementById("zwmbtilr").innerHTML ="现有<span class=\"tc1\">"+num+"</span>人阅读过该帖，评论<span class=\"tc1\">"+pinglun_num+"</span>条。"+xgti;
                </script>
                
                <div class="pager talc zwpager">
                    <span class="pagernums" id="newspage" data-page="news,tzzh,600256419_|332|30|1"></span>
                </div>
                
            </div>
            <style type="text/css">
                #zwbtextlink {
                    float: left;
                    width: 100%;
                    height: 29px;
                    margin-bottom: 5px;
                }

                    #zwbtextlink ul {
                        float: left;
                        padding-top: 8px;
                        width: 100%;
                    }

                        #zwbtextlink ul li {
                            float: left;
                            font-size: 14px;
                            padding: 0px 0px;
                        }

                            #zwbtextlink ul li a {
                                text-decoration: underline;
                                color: #333333;
                                margin-right: 7px;
                            }

                            #zwbtextlink ul li span.red a {
                                color: red;
                                font-weight: bold;
                                text-decoration: underline;
                            }
            </style>
            <div style="clear: both; height: 29px; border: 1px solid #D8E6FF; border-top: 0; padding: 0 0 5px 10px;">
                <div id="zwbtextlink">
                    <!-- 布告栏 -->
                    <ul><li><a href="http://acttg.eastmoney.com/pub/web_pc_gbzwy_plwzl_01_01_01_1" ><strong>委托队列惊现万手大单</strong></a>&nbsp;<span class="red"><a href="http://acttg.eastmoney.com/pub/web_jcb_gbzwy_zwd_01_01_02_1" ><strong>主力有大动作，10股望率先涨停！</strong></a></span>&nbsp;<a href="https://register.1234567.com.cn/reg/step1?spm=100005001.mw" ><strong>10秒开户抢占先机</strong></a>&nbsp;<span class="red"><a href="http://acttg.eastmoney.com/pub/web_nr_gbzwy_dby_01_01_01_0" ><strong>轻松获百万粉丝</strong></a></span></li></ul>
                </div>
            </div>


            <div class="gbbox1" id="sendnewt">
                <div class="gbboxt">评论该主题 <span class="appealspan"><a href="javascript:;" target="_self" id="appealuserlink">帖子不见了！怎么办？</a></span></div>
                <div class="gbboxtr"><span class="topbarlogin">作者：您目前是匿名发表 &nbsp; <a href="" id="bottomlogin" class="gubaloginlink"><strong>登录</strong></a> | <a href="" class="strlink gubareglink" id="bottomreg">5秒注册</a></span> <span class="topbarhaslogin">作者：<strong class="headerusername"><span class="username"></span></strong>，欢迎留言 <a href="javascript:;" class="logoutbtn" target="_self">退出</a></span> | <a href="/list,tzzh.html#sendnewt"><strong>发表新主题</strong></a></div>
                <div class="gbboxb">
                    <form name="gbsform" method="post" action="" id="gbsform" class="gbsform">
                        <div class="mtj1" id="yzmp">
                            <label for="" class="l tzla">内容：</label><textarea class="gbsformt1" id="gbtainput"></textarea>
                        </div>
                        <div class="mtj2">
                            <div class="editorfuns" id="editorfuns">
                                <a href="javascript:;" id="gbtainpubtn4" data-fun="face" target="_self"><em class="iconface"></em>表情</a>
                                <!--<a href="javascript:;" id="gbtainpubtn7" data-fun="stockcode" target="_self"><em class="iconstock"></em>股票</a>-->
                            </div>
                            <div class="gbsformbtns">
                                <a href="http://acttg.eastmoney.com/pub/web_nr_gbzwy_bmy_01_01_01_0" >实名认证 ，即可获得价值100元大礼包！</a></li></ul>
                                <span id="gdregbtn"></span>&nbsp;
                                <button type="submit" class="gbsformi3">发  布</button>
                            </div>
                            <div class="clear"></div>
                        </div>

                    </form>
                </div>
            </div>

            <div style="color: #888888; padding: 10px 0 0 0; clear: both; line-height: 120%;">
                提示：用户在社区发表的所有资料、言论等仅代表个人观点，与本网站立场无关，不对您构成任何投资建议。用户应基于自己的独立判断，自行决定证券投资并承担相应风险。<a href="http://guba.eastmoney.com/CommitmentLetter.aspx" target="_blank">《跟帖评论自律管理承诺书》</a>
            </div>

            
            <div class="siderg" style="padding-top: 10px; clear: both;">
                <iframe width="718" height="90" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" src="http://same.eastmoney.com/s?z=eastmoney&c=655&op=1"></iframe>
            </div>
            
        </div>
        <div id="sider"></div>
    </div>
    <div class="clear"></div>
    <div style="display:none">组合 id:200176280 </div>
    <div id="footer" class="gbbody">
    	<p class="splp"><a href="http://about.eastmoney.com/" target="_blank">关于我们</a>　　<a href="http://corp.eastmoney.com/Lianxi_guanggao.asp" target="_blank">广告服务</a>　　<a href="http://corp.eastmoney.com/Lianxi_lianxi.asp" target="_blank">联系我们</a>　　<a href="http://corp.eastmoney.com/zhaopin/zhaopin_1.asp" target="_blank">诚聘英才</a>　　<a href="http://corp.eastmoney.com/lianxi_mianze.asp" target="_blank">免责声明</a>　　<a href="http://corp.eastmoney.com/Lianxi_falvshengming.asp" target="_blank">法律声明</a>　　<a href="http://corp.eastmoney.com/Lianxi_zhengao.asp" target="_blank">征稿启事</a>　　<a href="http://corp.eastmoney.com/media.asp" target="_blank">友情链接</a></p>
    	<p class="sphp"></p>
        <p>违法和不良信息举报:021-54509988-2345/021-24099099　　　<a href="http://corp.eastmoney.com/Lianxi_liuyan.asp" target="_blank"><img src="http://g1.dfcfw.com/g1/comm/msg.gif" border="0" />意见与建议</a></p>
        <p class="sphp"></p>
        <p><img src="http://g1.dfcfw.com/g1/comm/icp.gif" />&nbsp;沪ICP证：沪B2-20070217&nbsp;&nbsp;<a style="display:inline-block;text-decoration:none;height:20px;line-height:20px;" href="http://shcainfo.miitbeian.gov.cn" target="_blank">网站备案号：沪ICP备05006054号-11</a>&nbsp;&nbsp;<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010402000119" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img src="/images/ghs.png" style="float:left;"/>沪公网安备 31010402000119号</a>&nbsp;&nbsp;版权所有：<a href="http://www.eastmoney.com" target="_blank">东方财富网</a></p>
        <p><a href="http://www.cyberpolice.cn/" target="_blank"><img src="http://g1.dfcfw.com/g1/comm/police.gif" border="0" /></a></p>
</div>
<!--172.17.25.42-->
    <div id="stockhqh" style="display: none;"></div>
    
    
    
    <script src="//gbfek.dfcfw.com/gubav5/js/gubabase_da218adfac.js"></script>
    <script src="http://emcharts.dfcfw.com/ec/2.4.4/emcharts.min.js"></script>
    <!-- <script src="build/js/news_m_043240ee42.js"></script> -->
    <script src="//gbfek.dfcfw.com/gubav5/js/news_m_043240ee42.js"></script>
    <script src="//gbfek.dfcfw.com/gubav5/js/module_d633a276f5.js"></script>
    <script src="//gbfek.dfcfw.com/gubav5/js/news_c_3ce50b57f2.js"></script>
    <script src="//gbfek.dfcfw.com/gubav5/modules/rightpromotion/rightpromotion.js?r=5"></script>
    <script src="count.aspx"></script>
    <script type="text/javascript">  var _cpyno = "c1"</script>
    <script type="text/javascript" src="http://js4.eastmoney.com/counter.js?c=t"></script>


    <script type="text/javascript" src="http://js3.eastmoney.com/js/gb_dcmap.js?mt=gubaarticle&odds=5000"></script>
    <script src="//gbfek.dfcfw.com/tg/EMBottomSearchTG/EMBottomSearchTG-1.0.3.min.js?v=1"></script>
    
    <script type="text/javascript">
        var newEMBottomSearchTG = new EMBottomSearchTG({
            main_width:1000,
            main_img: 'http://z1.dfcfw.com/2015/6/10/201506101029321460568336.jpg', //推广图片  imgurl
            link: 'http://stattg.eastmoney.com/10267' //推广链接  aurl
        });
        newEMBottomSearchTG.show();
    </script>
    <script type="text/javascript">
    window.emLeftBodyWidth = 1000; 
    window.emRightBodyWidth = 1040 ; 
    window.switchBackTop = 0; 
    window.emRightadDataType = "guba";

    window.dc_sampleRate=100;
</script>
<!-- <script type="text/javascript" src="http://emres.dfcfw.com/public/js/left.js" charset="utf-8"></script>
<script type="text/javascript" src="http://emres.dfcfw.com/public/js/em_news_fixed_right.js" charset="utf-8"></script> -->
<script type="text/javascript" src="http://cmsjs.eastmoney.com/analysis/emhotarea.min.js?v=20150923"></script>
<script>
	$().ready(function(){
		if(window.location.search.toLowerCase().indexOf("baidualaddin")>=0){
			jQuery.getScript("http://emres.dfcfw.com/public/js/aldtg.js");  
		}else{
			jQuery.getScript("http://emres.dfcfw.com/public/js/left.js");  
			jQuery.getScript("http://emres.dfcfw.com/public/js/em_news_fixed_right.js");  
		}
	})
</script>
<script type="text/javascript" src="http://emcharts.dfcfw.com/newsts/newsts.min.js" charset="utf-8"></script>

    
    <script type="text/javascript" src="http://bdstatic.eastmoney.com/web/prd/emtj_tracker.js"></script>
    
        <div style="width: 1px; height: 1px; overflow: hidden;">
        <iframe src="http://61.152.229.100/news.aspx?id=600256419&code=tzzh"></iframe>
    </div>
</body>
</html>


'''

Re_find_page_info = re.compile(r'data-page="(\S{2,6}\,\S{2,6}\,\d{6,12}\_)\|(\d{1,8})\|(\d{1,3})\|(\d{1,5})')
next_info_find_by_re = Re_find_page_info.findall(this_div)
print next_info_find_by_re[0]