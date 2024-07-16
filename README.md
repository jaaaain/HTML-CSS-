# HTML+CSS学习笔记

### ==HTML==

#### 基本组成

```html
<h1><h2><h3>...<h6>：标题</h1>
<p>文本内容</p>
```

#### 效果标签

```html
<br/>  换行
<hr/>	<!-- 水平线-->
&nbsp;<!--一个空格，html会忽略自己打的重复的空格和回车-->
```

#### 链接

```html
<img src="myimage.gif/png/jpeg(图片地址)" alt="下载失败/图像不可见" title="图像描述，鼠标滑过可见" />
<a href="https://www.baidu.com(目标网址)" title="鼠标滑过显示的文本" target="_self(默认在当前页面打开链接)"or"_blank(在新窗口打开链接)">百度</a>
<a id="标签1">标记一处地点</a>
<a href="#标签1">在别处转跳到标记处</a>
```

#### 语义化标签

```html
<span>无语义，用于设置单独的样式</span>
<div>独立的逻辑部分容器,看作空盒子，可划分栏目板块</div>
<header>头部标签</header>
<aside>侧边栏</aside>
<footer>底部标签</footer>
<section>代表一个区域</section>
	都与div同义，样式仍需要自己调整
```

#### 列表

```html
<ol>有序列表标签
	<li>1.有序列表</li>
	<li>2.有序列表</li>
	<li>3.有序列表</li>
</ol>
<ul>无序列表标签
	<li>·无序列表</li>
	<li>·无序列表</li>
	<li>·无序列表</li>
</ul>
```

#### 表格

```html
<table border="1"> <!--表格，数字表示边框厚度-->
	<caption>表格标题</caption>
	<tr>   <!--代表一行，几对tr就有几行-->
		<th>姓名</th> <!--代表一列（一行中的一个单元格），字体加粗（表头）-->
		<th>学号</th>
		<th>电话</th>
	</tr>
	<tr> 
		<td>张佳音</td><!--代表一列，正常字体，普通单元格-->
		<td>22050406</td>
		<td>18868143991</td>
	</tr>
</table>
```

#### 表单标签与交互

``` html
<form method="get/post(数据传递方式)" action="save.php(服务器文件,浏览者输入的数据被传到的地方)"> <!--表单-->
    
    <br/>
    <label for="username">密码：</label> <!--for需与下一致--><!--当单击label标签，自动转到输入框-->
    <input type="text" id="username" name="username" value="默认文本(文本输入框默认值，是真正的输入内容)" or placeholder="请输入关键字(输入框占位符，会消失)" />
    
    <br/>
    姓名：
    <input type="password" name="pass" />
    
    <br/>
    <input type="number" placeholder="请输入邮箱"/>  <!--输入框右侧有增减符号-->
    
    <br/>
    <input type="url" placeholder="请输入邮箱"/>  <!--数字框的值需以http://或者https://开头,且后面必须有内容,否则表单提交的时候会报错误提示。-->
    
    <br/>
    <input type="email" placeholder="请输入邮箱"/>
    
    <br/><!--文本域，大段文字输入-->
    <label>联系我们：</label>
    <textarea cols="50" rows="10" placeholder="请输入文字(这是会消失的提示内容)">在这里输入内容(这是真正的输入内容）</textarea>  <!--cols和rows可用css样式的width和height来代替-->
    
    <br/>
    <input type="radio(单选框)/checkbox(多选框)" value="1/2/...提交到服务器的数据（后台程序PHP使用）" name="名称，为控件命名，以备后台程序 ASP、PHP 使用" checked="chacked(当设置为 checked 时，该选项被默认选中)">  <!--注意:同一组的单选按钮，name 取值一定要一致,这样同一组的单选按钮才可以起到单选的作用。-->
    
    <br/><!--下拉菜单-->
    <select>
        <option value="向服务器提交的值" selected="selected(该选项默认选中)">选项(显示的值)</option>  
        <option value="提交值">选项</option>
        <option value="提交值">选项</option>
        <option value="提交值">选项</option>
    </select>
    
    <br/><!--提交按钮-->
    <input type="submit" value="提交(显示值)"/>
    <input type="button"/> <!--无效按钮-->
    
    <br/><!--重置按钮-->
    <input type="reset" value="重置">
</form>  <!--只有写到form里面才有效-->
```



#### *样例*

```html
<!DOCTYPE html> <!--声明文档类型为html5-->
<html>  <!--html文件的根标签-->
<head>  <!--头部标签，非网页内容-->
	<meta charset="UTF-8">  <!--meta提供与文档相关的名称-值对（元信息）--><!--charset字符集编码--><!--必备-->
	<title>浏览器标题</title>  <!--必备-->
	<style type="text/css">  
		span { 		
			color: red;
		}
	</style><!--书写CSS样式-->
</head>
<body>
	<h1>一级标题</h>
	<h2>二级标题</h>
	<header>头部标签</header> <!--可以用来写头部搜索条在的那部分-->
	<aside>侧边栏</aside>
    <form method="post" action="save.php">
    	<label for="username">用户名：</label>
    	<input type="text" name="username" />
        <br/>
    	<label for="pass">密码：</label>
    	<input type="password" name="pass" />
        <br/>
        男：
        <input type="redio" value="1" name="sex"/>
        女：
        <input type="redio" value="2" name="sex"/>
        <br/>
        选择地域：
        <select>
            <option value="浙江">浙江</option>
            <option value="上海">上海</option>
            <option value="江苏">江苏</option>
        </select>
        <br/>
        <input type="submit" value="登录" />
	</form>
	<p>&nbsp;&nbsp;&nbsp;&nbsp;1922年的春天，一个想要成名名叫尼克•卡拉威（托比•马奎尔Tobey Maguire 饰）的作家，离开了美国中西部，来到了纽约。那是一个道德感渐失，爵士乐流行，走私为王，股票飞涨的时代。为了追寻他的&nbsp;<span>美国梦</span>$nbsp;，他搬入纽约附近一海湾居住。</p>
	<section>代表一个区域</section> 
	<footer>底部标签</footer> <!--可以用来写底部小字-->
</body>
</html>
```



### ==CSS==

*全称：“层叠样式表 (Cascading Style Sheets)”*

修饰HTML样式

`选择符（又称选择器） { 属性：值; 属性：值;（样式声明）}`

```html
    <style type="text/css">
    p {	/*css注释*/
        font-size: 20px;
        /*设置文字字号*/
        color: red;
        /*设置文字颜色*/
        font-weight: bold;
        /*设置字体加粗*/
    }
    </style>
```

#### 形式

 + 内联式（行内）

   `<p style="color:red">这里文字是红色。</p>`

   ​	*注：style里的用引号引起来*

 + 嵌入式（head里）

   ```html
   <style type="text/css">
   span{
   color:red;
   }
   </style>
   ```

 + 外部式（外部文件）

   在`<head>`内（不是在`<style>`标签内）使用`<link>`标签将css样式文件链接到HTML文件内

   `<link href="base.css" rel="stylesheet" type="text/css" />`

   ​	*注：rel和type是固定写法不可修改*

#### 选择器

##### 1. 类选择器

`.类名{样式;}`

​	*注：前 ”  . " !!*

`<span class="类名">待修饰文本</span>`

##### 2. ID选择器

`#ID名{样式;}`

​	*注：前 “ # ” !!*

`<div id="ID名">待修饰文本</div>`

(span也一样)

###### 两者区别

1. ID只有一个！！只能用一次

2. class可以多次使用

3. 同个元素可有多个class

   `<span class="class1 class2">文本</span>`

   class1,class2共同修饰该文本

##### 1. 子选择器

`选择器名>子选择器名{样式;}`

​	*注：1. " > "	2.若子选择器仍为类，仍要加 " . "*

##### 2. 后代选择器（包含选择器）

`选择器名 后代选择器名{样式;}`

​	*注：“   ”（空格）*

###### 两者区别

1. " > "作用于元素的第一代后代，"   "(空格)作用于元素的所有后代

##### 通用选择器

功能最强大的选择器，匹配HTML中所有标签的元素

`*{样式;}`

##### 伪类选择器

`选择器名:hover{样式;}`

*注：" : "*

允许给html不存在的标签（标签的某种状态）设置样式

例：给html中一个标签元素的鼠标滑过的状态设置字体颜色`a:hover{color:red;}`

仅`:hover`可兼容所有浏览器，而`a:hover`最常用，兼容性最高

##### 分组选择器

`选择器1,选择器2{样式;}`

*注："  , "*

为html中多个标签元素设置同一个样式

例：`h1,span{color:red;}`相当于`h1{color:red;}和span{color:red;}`

##### 选择器优先级

内联样式 > id选择器 > 类选择器 > 标签选择器 > 通配符选择器

（越具体越优先）

###### 权值计算

标签：1  ；类选择器：10  ；ID选择器：100  ； 

###### 设置最高优先级

`选择器{样式!important;}`

*注：1. " ! "  2.在分号里面！！*

例：`p{color:red!important;}`

当网页制作者不设置css样式，浏览器使用默认样式，用户也可自己设置习惯的样式。这时样式优先级为：**浏览器默认的样式 < 网页制作者样式 < 用户自己设置的样式<!important**，!important权值高于一切

#### 字体样式

```html
<style type="text/css">
	p{
	font-family:"微软雅黑";sans-serif;
	font-size:20px;
	line-height:1.5em;
    font-weight:bold;	/*加粗*/
    font-style:normal/italic/oblique;
    /*normal为默认样式；italic为斜体，用于字体本身就有倾斜的样式；oblique为设置倾斜的字体，强制将字体倾斜*/
    color:#ff4399;
    color:rgb(255,67,153);
    color:rgb(100%,20%,50%);
	}
</style>
```

##### 缩写

```html
<style type="text/css">
    p{
        font:italic bold 12px/1.5em "宋体",sanc-serif;
        /*font-size与font-family必写;font-size与line-height中间要加入“/”斜扛*/
    }
</style>
```

#### 文本样式

```html
<style type="text/css">
    p{
        text-decoration:overline(上划线)/underline(下划线)/line-through(删除线)/none(标准文本);
        text-indent:2em;/*缩进；2em表文字的两倍*/
        line-height：2em;
        letter-spacing:0.5em;/*文字间隔或者字母间隔*/
        word-spacing:50px;/*英文单词之间的间距*/
        text-alige:center/left/right;/*文本对齐方式*/
    }
</style>
```

#### 盒模型

在CSS中，html中的标签元素大体被分为三种不同的类型：**块状元素**、**内联元素(又叫行内元素)**和**内联块状元素**。

+ 常用的块状元素有：

`<div> <p> <h1>..<h6> <ol> <ul> <dl> <table> <address> <blockquote> <form>`

+ 常用的内联元素有：

`<a> <span> <br> <i> <em> <strong> <label> <q> <var> <cite> <code>`

+ 常用的内联块状元素有：

`<img> <input>`

##### 块状元素

​	转换：`display:block;`

`<div> <p> <h1>..<h6> <ol> <ul> <dl> <table> <address> <blockquote> <form>`

###### 特点：

1. 每个块级元素都从新的一行开始，并且其后的元素也另起一行。（真霸道，一个块级元素独占一行）

   > 在父容器中`display:flex`（弹性盒模型）可把块状元素排在一排显示

2. 元素的高度、宽度、行高以及顶和底边距都可设置。

3. 元素宽度在不设置的情况下，是它本身父容器的100%（和父元素的宽度一致），除非设定一个宽度。

##### 内联元素

​	转换：`display:inline;`

`<a> <span> <br> <i> <em> <strong> <label> <q> <var> <cite> <code>`

###### 特点：

1. 和其他元素都在一行上；

   > 内联元素间距问题：使用float脱离文档：`float:left`

2. 元素的高度、宽度及顶部和底部边距**不可**设置；

3. 元素的宽度就是它包含的文字或图片的宽度，不可改变

##### 内联块状元素

转换：`display:inline-block;`

`<img> <input>`

###### 特点：

1. 和其他元素都在一行上；

2. 元素的高度、宽度、行高以及顶和底边距都可设置。

##### 隐形

`display:none;`

##### 盒模型建立

![img](https://img.mukewang.com/543b4cae0001b34304300350.jpg)

```html
<style type="text/css">
div{
	width:200px;
    height:200px;
    
    border:1px solid red;
    /*	border-width:1px;
    	border-style:solid(实线)/dotted(点线)/dashed(虚线);
    	border-color:red;*/
    border-bottom:1px dashed #ccc;/*下框线*/
    border-radius:20px 10px 15px 30px;/*设置圆角，从左上顺时针方向*/
    /*	border-top-left-radius: 20px;
   		border-top-right-radius: 10px;
	   	border-bottom-right-radius: 15px;
   		border-bottom-left-radius: 30px;*/
    border-radius:10px;/*四个角都为10px*/
    border-radius:10px 20px;/*10px 20px 1
    0px 20px*/
    border-radius:50%;
    /*正方形设置圆角为宽度一半为圆形*/
    
    padding:20px 10px 15px 30px;/*设置内边距填充，从上顺时针方向*/
    /*	padding-top:20px;
	   	padding-right:10px;
   		padding-bottom:15px;
   		padding-left:30px;*/
    padding:10px;/*填充都为10px*/
    padding:10px 20px;/*10px 20px 1
    0px 20px*/
    
   	margin:10px;/*设置同padding，padding在边框里，margin在边框外。*/
    
    background-color:red;
}
</style>
```

#### 布局模型

在网页中，元素有三种布局模型：

1. 流动模型（Flow）
2. 浮动模型 (Float）
3. 层模型（Layer）

##### 流动模型（Flow）

默认

###### 特点：

1. 块状元素都在所处包含元素内自上而下按顺序垂直分布，因为在默认状态下，块状元素的宽度都为100%。
2. 内联元素都会在所处包含元素内从左到右水平分布。

##### 浮动模型（Float）

任何元素在默认情况下是不能浮动的，设置元素浮动就可以让两个块状元素并排显示

```html
#div1{float:left;}
#div2{float:right;}
```

##### 层模型（Layer）

每个图层精确定位操作，一般在网页上局部使用层布局

层模型有三种定位形式：

1. 绝对定位(position: absolute)
2. 相对定位(position: relative)
3. 固定定位(position: fixed)

###### 绝对定位

`position:absolute`

`right:100px;top:100px;`

然后用left、right、top、bottom属性相对于其最接近的一个**具有定位属性的父包含块**进行绝对定位

父包含块可通过`position:relative;`设置定位属性，以其显示位置进行定位

###### 相对定位

`position: relative`

通过left、right、top、bottom属性确定元素在**正常文档流中相对原位置**的偏移位置

显示的产生了偏移，但是元素实质位置还保留着

###### 固定定位

`position: fixed`

相对移动的坐标是视图（**网页窗口**）本身，不会受文档流动影响，与`background-attachment:fixed;`属性功能相同

#### 弹性盒模型

`display:flex`

1. 设置display: flex属性可以把块级元素在一排显示。
2. flex需要添加在父元素上，改变子元素的排列顺序。
3. 默认为从左往右依次排列,且和父元素左边没有间隙。

##### 横轴操作：

`justify-content:flex-start(起点对齐)/flex-end(右对齐)/center(居中)/space-between(两端对齐，项目间间隔相等)/space-around(项目两侧占有空间相等);`

##### 纵轴操作：

`align-items:flex-start(默认,左对齐)/flex-end(左下对齐)/center(左侧中点对齐)/baseline(项目的第一行文字的基线（上线）对齐)/stretch(默认,如果项目未设置高度或设为auto，将占满整个容器的高度);`

##### 占比设置：

1. flex属性的值只能是**正整数**,表示占比多少。
2. 给子元素设置了flex之后,其宽度属性会失效。

```html
<head>
<style type="text/css">
.box {
    height: 300px;
    background: blue;
    display: flex;
    justify-content:center;/*失效*/
    align-items:center;/*有效*/
}

.box div {
    width: 200px;
    height: 200px;
}

.box1 {
    flex: 1;
    background: red;
}

.box2 {
    flex: 3;
    background: orange;
}

.box3 {
    flex: 2;
    background: green;
}
</style>
</head>

<body>
    <div class="box">
        <div class="box1">flex:1</div>
        <div class="box2">flex:3</div>
        <div class="box3">flex:2</div>
    </div>
</body>
```

#### 水平居中设置

##### 行内元素

 `text-align:center`

如果被设置元素为文本、图片等行内元素时，水平居中是通过给父元素设置 `text-align:center` 来实现的。

##### 块状元素

###### 定宽块状元素

条件：1. 定宽   2.块状

```html
margin:20px auto;/*上下值可随意设置，水平居中即可*/
/* 	margin-left:auto;
	margin-right:auto; */
```

可以通过设置“左右margin”值为“auto”来实现居中

###### 不定宽块状元素

##### 盒子

`transform: translate(-50%, -50%);`

```html
<head>
    <style type="text/css">
    .box {
        border: 1px solid #00ee00;
        height: 300px;
        position: relative;/*层模型相对定位*/
    }

    .box1 {
        border: 1px solid red;
        position: absolute;/*层模型绝对定位*/
        top: 50%;
        left: 50%;/*中心位置*/
        transform: translate(-50%, -50%);/*减掉自身宽高的一半*/
    }
    </style>
</head>
```

#### *样例*

```html
<head>
        <meta charset="UTF-8">
        <title>Html和CSS的关系</title>
        <style type="text/css">
        h1{
            color: red; /*字体颜色*/
            border: 3px solid blue; /*border：边框；3px：框线粗细；solid：？？？；blue：框线颜色 */
            width:140px;
            height:90px;
            background-color:yellow; /*背景色*/
        }/*h1标题设置*/
        p{
            font-size:12px; /*字体大小*/            			color:#FF4399;
            text-align:center; /*居中*/
        }/*文本设置*/
        </style>
    </head>
```





