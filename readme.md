</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>two_step_pca</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:d%3A%5Cprojects%5Cts-pca%5Ctwo_step_pca.py">d:\projects\ts-pca\two_step_pca.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="numpy.html">numpy</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-calcA"><strong>calcA</strong></a>(data, lag, D)</dt><dd><tt>Calculates&nbsp;matrix&nbsp;A,&nbsp;which&nbsp;represents&nbsp;dynamic&nbsp;part&nbsp;of&nbsp;the&nbsp;model<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;-&nbsp;numpy&nbsp;array&nbsp;with&nbsp;input&nbsp;data<br>
&nbsp;&nbsp;&nbsp;&nbsp;lag&nbsp;-&nbsp;lag&nbsp;parameter&nbsp;of&nbsp;the&nbsp;model<br>
&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;-&nbsp;time&nbsp;difference&nbsp;parameter<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;-&nbsp;numpy&nbsp;array&nbsp;describing&nbsp;dynamic&nbsp;part&nbsp;of&nbsp;the&nbsp;TS-PCA</tt></dd></dl>
 <dl><dt><a name="-computeSPE"><strong>computeSPE</strong></a>(T)</dt><dd><tt>Computes&nbsp;SPE&nbsp;metric<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;T&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;score&nbsp;matrix,&nbsp;unlike&nbsp;in&nbsp;Hotelling's&nbsp;T2&nbsp;you&nbsp;use&nbsp;"m-l"&nbsp;PCs&nbsp;here,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;so&nbsp;T&nbsp;here&nbsp;is&nbsp;all&nbsp;principal&nbsp;components&nbsp;you&nbsp;didnt&nbsp;use&nbsp;in&nbsp;T2&nbsp;calculations.<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;SPE&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;Squared&nbsp;Prediction&nbsp;Error</tt></dd></dl>
 <dl><dt><a name="-computeT2"><strong>computeT2</strong></a>(T, E)</dt><dd><tt>Computes&nbsp;T2&nbsp;metric<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;T&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;score&nbsp;matrix&nbsp;(or&nbsp;principal&nbsp;components,&nbsp;it&nbsp;is&nbsp;the&nbsp;same),&nbsp;usually&nbsp;you&nbsp;pick&nbsp;first&nbsp;"l"&nbsp;PCs,&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;which&nbsp;explain&nbsp;most&nbsp;variance<br>
&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;-&nbsp;eigenvalues&nbsp;which&nbsp;correspond&nbsp;to&nbsp;T<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;T2&nbsp;-&nbsp;Hotelling's&nbsp;T2&nbsp;metric</tt></dd></dl>
 <dl><dt><a name="-delta"><strong>delta</strong></a>(data, D)</dt><dd><tt>Calculates&nbsp;matrix&nbsp;dX&nbsp;=&nbsp;X(t)&nbsp;-&nbsp;X(t-D)<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;-&nbsp;numpy&nbsp;array&nbsp;with&nbsp;input&nbsp;data&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;-&nbsp;time&nbsp;difference&nbsp;between&nbsp;the&nbsp;samples<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;dX&nbsp;-&nbsp;numpy&nbsp;array</tt></dd></dl>
 <dl><dt><a name="-dividePCs"><strong>dividePCs</strong></a>(T, E, var_explained, var_explained_required)</dt><dd><tt>Divides&nbsp;Principal&nbsp;component&nbsp;matrix&nbsp;into&nbsp;two&nbsp;matricies,&nbsp;depending&nbsp;on&nbsp;how&nbsp;much&nbsp;variance,<br>
must&nbsp;be&nbsp;explained.&nbsp;You&nbsp;can&nbsp;think&nbsp;of&nbsp;this&nbsp;function&nbsp;the&nbsp;same&nbsp;way,&nbsp;as&nbsp;n_pca&nbsp;(or&nbsp;n_components)&nbsp;in&nbsp;sklearn.decomposition.PCA<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;T&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;score&nbsp;matrix<br>
&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;eigenvalues<br>
&nbsp;&nbsp;&nbsp;&nbsp;var_explained&nbsp;-&nbsp;list,&nbsp;consists&nbsp;of&nbsp;values,&nbsp;which&nbsp;show&nbsp;how&nbsp;much&nbsp;variance&nbsp;each&nbsp;PC&nbsp;explains<br>
&nbsp;&nbsp;&nbsp;&nbsp;var_explained_required&nbsp;-&nbsp;float,&nbsp;how&nbsp;much&nbsp;variance&nbsp;must&nbsp;be&nbsp;explained&nbsp;by&nbsp;all&nbsp;selected&nbsp;PCs<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;T_l&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;score&nbsp;matrix&nbsp;with&nbsp;top&nbsp;l&nbsp;PCs,&nbsp;which&nbsp;explain&nbsp;required&nbsp;amount&nbsp;of&nbsp;variance<br>
&nbsp;&nbsp;&nbsp;&nbsp;E_l&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;eigen&nbsp;values&nbsp;which&nbsp;correspond&nbsp;to&nbsp;T_l&nbsp;score&nbsp;matrix<br>
&nbsp;&nbsp;&nbsp;&nbsp;T_rest&nbsp;-&nbsp;numpy&nbsp;array,&nbsp;score&nbsp;matrix&nbsp;containing&nbsp;all&nbsp;the&nbsp;PCs&nbsp;not&nbsp;included&nbsp;in&nbsp;T_l,&nbsp;it&nbsp;is&nbsp;needed&nbsp;for&nbsp;SPE&nbsp;calculations</tt></dd></dl>
 <dl><dt><a name="-fit_transform"><strong>fit_transform</strong></a>(data, q, D)</dt><dd><tt>Fit&nbsp;TS-PCA&nbsp;model&nbsp;with&nbsp;data&nbsp;<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;-&nbsp;numpy&nbsp;array&nbsp;with&nbsp;input&nbsp;data<br>
&nbsp;&nbsp;&nbsp;&nbsp;q&nbsp;-&nbsp;lag,&nbsp;if&nbsp;not&nbsp;specified&nbsp;will&nbsp;use&nbsp;the&nbsp;one&nbsp;from&nbsp;constructor<br>
&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;-&nbsp;time&nbsp;difference&nbsp;between&nbsp;two&nbsp;data&nbsp;samples&nbsp;used&nbsp;for&nbsp;estimating&nbsp;dynamic&nbsp;part,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;not&nbsp;specified&nbsp;the&nbsp;one&nbsp;from&nbsp;constructor&nbsp;is&nbsp;used<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;U&nbsp;-&nbsp;innovation&nbsp;part&nbsp;(numpy&nbsp;array)<br>
&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;-&nbsp;numpy&nbsp;array&nbsp;describing&nbsp;dynamic&nbsp;part&nbsp;of&nbsp;the&nbsp;model<br>
&nbsp;&nbsp;&nbsp;&nbsp;tildaX&nbsp;-&nbsp;time&nbsp;shifted&nbsp;input&nbsp;numpy&nbsp;array</tt></dd></dl>
 <dl><dt><a name="-pca"><strong>pca</strong></a>(data)</dt><dd><tt>Usual&nbsp;PCA&nbsp;decomposition&nbsp;which&nbsp;returns&nbsp;all&nbsp;intermediate&nbsp;parameters<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;-&nbsp;numpy&nbsp;array&nbsp;with&nbsp;input&nbsp;data&nbsp;(should&nbsp;be&nbsp;already&nbsp;with&nbsp;zero&nbsp;mean&nbsp;and&nbsp;unit&nbsp;variance)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;most&nbsp;probably&nbsp;you&nbsp;want&nbsp;to&nbsp;pass&nbsp;U(innovation&nbsp;part)&nbsp;here<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;T&nbsp;-&nbsp;score&nbsp;matrix&nbsp;(Principal&nbsp;components)<br>
&nbsp;&nbsp;&nbsp;&nbsp;P&nbsp;-&nbsp;loading&nbsp;matrix&nbsp;(eigenvectors)<br>
&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;-&nbsp;eigenvalues<br>
&nbsp;&nbsp;&nbsp;&nbsp;var_explained&nbsp;-&nbsp;variance&nbsp;explained&nbsp;for&nbsp;each&nbsp;principal&nbsp;component</tt></dd></dl>
 <dl><dt><a name="-shift_data"><strong>shift_data</strong></a>(data, lag)</dt><dd><tt>Creates&nbsp;a&nbsp;matrix&nbsp;based&nbsp;on&nbsp;input&nbsp;data&nbsp;and&nbsp;selected&nbsp;lag<br>
Corresponds&nbsp;to&nbsp;~X&nbsp;in&nbsp;the&nbsp;paper<br>
Arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;-&nbsp;numpy&nbsp;array&nbsp;with&nbsp;input&nbsp;data<br>
&nbsp;&nbsp;&nbsp;&nbsp;lag&nbsp;-&nbsp;time&nbsp;lag&nbsp;parameter<br>
Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;tildaX&nbsp;-&nbsp;~X&nbsp;from&nbsp;the&nbsp;paper</tt></dd></dl>
</td></tr></table>
</body></html>