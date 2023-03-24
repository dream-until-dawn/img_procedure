<h1>pfp类NFT图片合成-支持2-20个图层</h1>
<h2>开发环境</h2>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang">python</span><span class="code-block-header__copy">复制代码</span></div><code class="hljs code-block-body python">python <span class="hljs-number">3.9</span><span class="hljs-number">.12</span>
</code></pre>
<p>所需python库：</p>
<ul>
<li>Pillow  9.1.0</li>
</ul>
<p>其安装指令:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang">bash</span><span class="code-block-header__copy">复制代码</span></div><code class="hljs code-block-body bash">pip install Pillow==9.1.0
</code></pre>
<h2>使用方法</h2>
<ol>
<li>确保已安装python和Pillow库</li>
<li>在coverage_n图层文件夹下放置pfp类NFT的各个部件。
<ul>
<li>其中1为最底层,20为最高层。</li>
<li>文件夹不放置图片脚本就会略过。</li>
<li>文件夹原有图片为测试用，放心删除。</li>
<li>图片格式只试过.png格式，其它有透明通道的图片格式未试过。</li>
</ul>
</li>
<li>在项目文件下运行 <code>python start.py</code> 即可。</li>
<li>输出的图片文件保存在 save 文件夹。</li>
</ol>