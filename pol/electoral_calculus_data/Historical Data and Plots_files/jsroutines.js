// jsroutines.js
// (C)2020 Electoral Calculus Ltd

// Sections
// 1. PAGE START AND END
// 2. FORM HANDLING
// 3. BRICK CODE
// 4. CustomSelect and DropDown
// 5. UTILITIES
// 6. GENERAL DATALOAD FUNCTIONS
// 7. GEOSERVER ROUTINES

// 1. PAGE START AND END ==================================
// subroutine of PageStart
function AddMetaNameContent(headelt, name, content)
{
	var metaelt = document.createElement("META");
	metaelt.setAttribute("name", name);
	metaelt.setAttribute("content", content);
	headelt.appendChild(metaelt);
	return;
}

// Main Routines to create and populate page layout
function PageStart(prefix)
{
	if (prefix == null) { prefix = ""; }
	
	var breadcrumb_html = BreadcrumbsHTML(prefix);
	
	// add some META tags to the HEAD node
	var headelt = document.getElementsByTagName("HEAD")[0];
	AddMetaNameContent(headelt, "HandheldFriendly", "true");
	AddMetaNameContent(headelt, "apple-mobile-web-app-capable", "yes");
	AddMetaNameContent(headelt, "viewport", "width=device-width, initial-scale=1.0");
	
	var html = `
<DIV id="wholepage">
<DIV id="topbanner">
	<div id="banner_logo">
		<A href="${prefix}homepage.html"><IMG src="${prefix}ECLogo.svg"></A>
	</div>
	<div class="banner_menu notmobile">
		<DIV class="banner_item dropdown" onclick="gourl('${prefix}services_general.html');" onmouseover="dd_click(event);" onmouseout="dd_click(event);">
			<A href="${prefix}services_general.html">Services</A>
			<UL onclick="event.stopPropagation();">
				<LI onclick="gourl('${prefix}services_general.html');">
					<A href="${prefix}services_general.html">Services home</A></LI>
				<LI onclick="gourl('${prefix}services_polling.html');">
					<A href="${prefix}services_polling.html">Polling Regression Analysis</A></LI>
				<LI onclick="gourl('${prefix}services_electoral.html');">
					<A href="${prefix}services_electoral.html">Election Predictions</A></LI>
				<LI onclick="gourl('${prefix}services_data.html');">
					<A href="${prefix}services_data.html">Electoral and Political Data</A></LI>
				<LI onclick="gourl('${prefix}services_solutions.html');">
					<A href="${prefix}services_solutions.html">Customised Maps &amp; Solutions</A></LI>
				<LI onclick="gourl('${prefix}services_casestudy_ge2019.html');">
					<A href="${prefix}services_casestudy_ge2019.html">Case Studies</A></LI>
			</UL>
		</DIV>
		<DIV class="banner_item dropdown" onclick="gourl('${prefix}prediction_home.html');" onmouseover="dd_click(event);" onmouseout="dd_click(event);">
			<A href="${prefix}prediction_home.html">UK Predictions</A>
			<UL onclick="event.stopPropagation();">
				<LI onclick="gourl('${prefix}prediction_home.html');">
					<A href="${prefix}prediction_home.html">Prediction home</A></LI>
				<LI onclick="gourl('${prefix}newseatlookup.html');">
					<A href="${prefix}newseatlookup.html">Your Seat</A></LI>
				<LI onclick="gourl('${prefix}userpoll.html');">
					<A href="${prefix}userpoll.html">Your Prediction</A></LI>
				<LI onclick="gourl('${prefix}prediction_main.html');">
					<A href="${prefix}prediction_main.html">Our prediction</A></LI>
				<LI onclick="gourl('${prefix}scotland.html');">
					<A href="${prefix}scotland.html">Scotland</A></LI>
				<LI onclick="gourl('${prefix}northernireland.html');">
					<A href="${prefix}northernireland.html">Northern Ireland</A></LI>
			</UL>
		</DIV>
		<DIV class="banner_item dropdown" onclick="gourl('${prefix}resources_home.html');" onmouseover="dd_click(event);" onmouseout="dd_click(event);">
			<A href="${prefix}resources_home.html">UK Resources</A>
			<UL onclick="event.stopPropagation();">
				<LI onclick="gourl('${prefix}resources_home.html');">
					<A href="${prefix}resources_home.html">Resources home</A></LI>
				<LI onclick="gourl('${prefix}boundaries2023.html');">
					<A href="${prefix}boundaries2023.html">New Boundaries 2023</A></LI>
				<LI onclick="gourl('${prefix}map_home.html');">
					<A href="${prefix}map_home.html">Maps</A></LI>
				<LI onclick="gourl('${prefix}pol3d_main.html');">
					<A href="${prefix}pol3d_main.html">3D Politics</A></LI>
				<LI onclick="gourl('${prefix}polls.html');">
					<A href="${prefix}polls.html">Polls</A></LI>
				<LI onclick="gourl('${prefix}flatfile.html');">
					<A href="${prefix}flatfile.html">Historical Data</A></LI>
			</UL>
		</DIV>
		<DIV class="banner_item dropdown" onclick="gourl('${prefix}blogs/index.html');" onmouseover="dd_click(event);" onmouseout="dd_click(event);">
			<A href="${prefix}blogs/index.html">Articles</A>
			<UL onclick="event.stopPropagation();">
				<LI onclick="gourl('${prefix}blogs/index.html');">
					<A href="${prefix}blogs/index.html">Articles home</A></LI>
				<LI onclick="gourl('${prefix}sitemap.html');">
					<A href="${prefix}sitemap.html">Sitemap</A></LI>
				<LI onclick="gourl('${prefix}faq.html');">
					<A href="${prefix}faq.html">FAQs</A></LI>
			</UL>
		</DIV>
		<DIV class="banner_item dropdown search" onclick="dd_click(event);">
			<IMG src="${prefix}icon_search_black.svg" >
			<UL onclick="event.stopPropagation();">
				<LI>
					<P>Search the Electoral Calculus site:</P>
					<FORM id="form_search" action="${prefix}cgi-bin/search.py">
						<DIV class="input_button">
							<INPUT type="text" name="q" id="search_input" maxlength="255"
								placeholder="Enter search string" >
							<DIV class="button" onclick="form_go('form_search');"><IMG src="${prefix}icon_search_white.svg"></DIV>
						</DIV>
					</FORM>
				</LI>
			</UL>
		</DIV>
		<DIV class="banner_item button" id="banner_contact" onclick="gourl('${prefix}services_contact.html');">
			<A href="${prefix}services_contact.html">Contact</A></DIV>
	</div> <!-- banner_menu -->
	<div class="mobileonly kct_toggle nmbutton">
		<div></div>
		<div onclick="ShowHideDiv(this,'navmobile','&emsp;','&emsp;','.kct_toggle:show');">&emsp;</div>
	</div>
</DIV> <!-- topbanner -->
<DIV class="ShowHide_Hide" id="navmobile">
	<DIV id="nm_search">
		<FORM id="form_search2" action="${prefix}cgi-bin/search.py">
			<DIV class="input_button">
				<INPUT type="text" name="q" id="search_input2" maxlength="255" class="fullwidth"
					placeholder="Enter search string" >
				<DIV class="button" onclick="form_go('form_search2');"><IMG src="${prefix}icon_search_white.svg"></DIV>
			</DIV>
		</FORM>
	</DIV>
	<DIV class="nm_accordion">
		<DIV class="kct_toggle">
		<DIV><A href="${prefix}services_general.html">Services</A></DIV>
		<DIV onclick="ShowHideDivNM(this,'nm_services');">&emsp;</DIV></DIV>
		<DIV id="nm_services" class="ShowHide_Hide">
			<UL>
			<LI onclick="gourl('${prefix}services_general.html');">
				<A href="${prefix}services_general.html">Services home</A></LI>
			<LI onclick="gourl('${prefix}services_polling.html');">
				<A href="${prefix}services_polling.html">Polling Regression Analysis</A></LI>
			<LI onclick="gourl('${prefix}services_electoral.html');">
				<A href="${prefix}services_electoral.html">Election Predictions</A></LI>
			<LI onclick="gourl('${prefix}services_data.html');">
				<A href="${prefix}services_data.html">Electoral and Political Data</A></LI>
			<LI onclick="gourl('${prefix}services_solutions.html');">
				<A href="${prefix}services_solutions.html">Customised Maps &amp; Solutions</A></LI>
			<LI onclick="gourl('${prefix}services_casestudy_ge2019.html');">
				<A href="${prefix}services_casestudy_ge2019.html">Case Studies</A></LI>
			</UL>
		</DIV>
	</DIV>
	<DIV class="nm_accordion">
		<DIV class="kct_toggle">
		<DIV><A href="${prefix}prediction_home.html">UK Predictions</A></DIV>
		<DIV onclick="ShowHideDivNM(this,'nm_prediction');">&emsp;</DIV></DIV>
		<DIV id="nm_prediction" class="ShowHide_Hide">
			<UL>
				<LI onclick="gourl('${prefix}prediction_home.html');">
					<A href="${prefix}prediction_home.html">Prediction home</A></LI>
				<LI onclick="gourl('${prefix}newseatlookup.html');">
					<A href="${prefix}newseatlookup.html">Your Seat</A></LI>
				<LI onclick="gourl('${prefix}userpoll.html');">
					<A href="${prefix}userpoll.html">Your Prediction</A></LI>
				<LI onclick="gourl('${prefix}prediction_main.html');">
					<A href="${prefix}prediction_main.html">Our prediction</A></LI>
				<LI onclick="gourl('${prefix}scotland.html');">
					<A href="${prefix}scotland.html">Scotland</A></LI>
				<LI onclick="gourl('${prefix}northernireland.html');">
					<A href="${prefix}northernireland.html">Northern Ireland</A></LI>
			</UL>
		</DIV>
	</DIV>
	<DIV class="nm_accordion">
		<DIV class="kct_toggle">
		<DIV><A href="${prefix}resources_home.html">UK Resources</A></DIV>
		<DIV onclick="ShowHideDivNM(this,'nm_resources');">&emsp;</DIV></DIV>
		<DIV id="nm_resources" class="ShowHide_Hide">
			<UL>
				<LI onclick="gourl('${prefix}resources_home.html');">
					<A href="${prefix}resources_home.html">Resources home</A></LI>
				<LI onclick="gourl('${prefix}boundaries2023.html');">
					<A href="${prefix}boundaries2023.html">New Boundaries 2023</A></LI>
				<LI onclick="gourl('${prefix}map_home.html');">
					<A href="${prefix}map_home.html">Maps</A></LI>
				<LI onclick="gourl('${prefix}pol3d_main.html');">
					<A href="${prefix}pol3d_main.html">3D Politics</A></LI>
				<LI onclick="gourl('${prefix}polls.html');">
					<A href="${prefix}polls.html">Polls</A></LI>
				<LI onclick="gourl('${prefix}flatfile.html');">
					<A href="${prefix}flatfile.html">Historical Data</A></LI>
			</UL>
		</DIV>
	</DIV>
	<DIV class="nm_accordion">
		<DIV class="kct_toggle">
		<DIV><A href="${prefix}blogs/index.html">Articles</A></DIV>
		<DIV onclick="ShowHideDivNM(this,'nm_articles');">&emsp;</DIV></DIV>
		<DIV id="nm_articles" class="ShowHide_Hide">
			<UL>
				<LI onclick="gourl('${prefix}blogs/index.html');">
					<A href="${prefix}blogs/index.html">Articles home</A></LI>
				<LI onclick="gourl('${prefix}sitemap.html');">
					<A href="${prefix}sitemap.html">Sitemap</A></LI>
				<LI onclick="gourl('${prefix}faq.html');">
					<A href="${prefix}faq.html">FAQs</A></LI>
			</UL>
		</DIV>
	</DIV>
	<DIV id="nm_contact"><INPUT type="button" class="button fullwidth" value="Contact" onclick="gourl('${prefix}services_contact.html');"></DIV>
</DIV>
${breadcrumb_html}
<DIV id="header2" class="header2 hide">
	<H1 id="h2_title">TITLE</H1>
	<OBJECT data="${prefix}icon_fingers128.svg" type="image/svg+xml"
		onload="finger_init(this, '#a0ffffff', 217);"></OBJECT>
</DIV>
<DIV class="main_outer">
	<DIV id="main">
	`;
	document.write(html);
	
	// search through all the dropdowns and mark the one corresponding to the current location
	MarkHighlight(".dropdown LI");
	MarkHighlight("#navmobile LI");
	
	return;
}

// subroutine of PageStart
function MarkHighlight(queryselector)
{
	var ddlis = document.querySelectorAll(queryselector);
	var thispath = window.location.pathname;
	var thisfile = thispath.split('/').slice(-1)[0];
	for (var i=0;i<ddlis.length;i++)
	{
		var onclickattr = ddlis[i].getAttribute('onclick');
		if (onclickattr == null) { continue; }
		var onclickpath = onclickattr.split("'")[1];
		var onclickfile = onclickpath.split('/').slice(-1)[0];
		if (onclickfile == thisfile)
		{
			ddlis[i].classList.add("highlight");
		}
	}
	return;
}

// subroutine of PageStart
// will look for global variable "breadcrumbs" which should be declared in the header of the HTML file
function BreadcrumbsHTML(prefix)
{
	if (typeof breadcrumbs == "undefined") { return '<DIV id="breadcrumbs" class="empty"></DIV>'; }
	var outstr = '<DIV id="breadcrumbs"><DIV>'
	for (var i=0;i<breadcrumbs.length-1;i++)
		outstr = outstr + '<A href="' + prefix + breadcrumbs[i][1] + '">' + breadcrumbs[i][0] + '</A> / ';
	outstr = outstr + breadcrumbs[breadcrumbs.length-1][0] + '</DIV></DIV>';
	return outstr;
}

// subroutine of SetElementById
function RemoveElement(elt)
{
	elt.parentNode.removeChild(elt);
	return;
}

// subroutine of SetStrapTitle
// sets innerHTHML of element to contents. If contents==null, then element is deleted
function SetElementById(elid, contents)
{
	var elt = document.getElementById(elid);
	if (contents != null) {	elt.innerHTML = contents; } else { RemoveElement(elt); }
	return;
}

// subroutine of PageEnd
// writes to strap at top of page. Any input which is null will be deleted from strap
function SetStrapTitle(Title)
{
	SetElementById("h2_title", Title);
	document.getElementById("header2").classList.remove("hide");
	return;
}

// subroutine of PageEnd
function ServicesBrick(prefix = "")
{
	var html = `
		<DIV class="brick services" onclick="gourl('${prefix}services_together.html');" >
			<P class="strap mobileonly">SERVICES</P>
			<H3>Affordable MRP Regression Polling and Consultancy</H3>
			<P>We're a quantitative political consultancy specialising in analysis and
			models for electoral and market research projects.
			Discover how we can work together.</P>
			<BR>
			<DIV class="button2 width177 tight notmobile">
				<A href="${prefix}services_together.html"><B>Let's work together</B></A></DIV>
			<OBJECT data="${prefix}icon_fingers128.svg" type="image/svg+xml"
				onload="finger_init(this, '#80aa1bff', 0);" class="notmobile"></OBJECT>
			<P class="mobileonly"><A href="${prefix}services_together.html" class="onblue">Find out more</A></P>
			<OBJECT data="${prefix}icon_fingers128.svg" type="image/svg+xml"
				onload="finger_init(this, '#ffffffff', 0);" class="mobileonly"></OBJECT>
		</DIV> <!-- end of brick services -->
`;
	return html;
}

// subroutine of PageEnd
function SubscribeBrick(prefix = "")
{
	var html = `
		<DIV class="brick updates nohover">
			<P class="strap">EMAIL UPDATES</P>
			<H3>Want To Stay Updated?</H3>
			<P>Receive an e-mail notification every time the site is updated.</P>
			
			<FORM method="post" action="${prefix}simplemailing/process.php" id="form_subscribe"
				onsubmit="return SFSubmitForm(this);">		
				<P><B>Enter your name:</B></P>			
				<DIV>
					<INPUT type="text" class="fullwidth" name="username" maxlength="100" placeholder="Your Name"
						onkeydown="NoSubmit(event);">
				</DIV>
				<DIV id="err_username" class="inputerror"></DIV>
				<P><B>Enter your email:</B></P>
				<DIV class="input_button">
					<INPUT type="text" class="fullwidth" name="address" maxlength="100" 
					placeholder="Email@address"><INPUT type="submit" class="button" value="Go">
				</DIV>
				<DIV id="err_address" class="inputerror"></DIV>
				<INPUT type="hidden" name="subtype" value="sub">
			</FORM>

			<P class="small">You can <A href="${prefix}subscribe.html">unsubscribe</A>
			from our emails at any time. By proceeding you
			agree to our <A href="${prefix}subscribe.html">email terms and conditions</A>
			and <A href="${prefix}dataprivacy.html">privacy policy</A>.</P>
		</DIV> <!-- end of brick -->
`;
	return html;
}

// Main function at end of page
function PageEnd(prefix = "", control="")
{
	if (prefix == null) { prefix = ""; }
	var controllist = control.split(',');
	var todaydate = new Date();
	var year = todaydate.getFullYear();
	// try for strap
	var titleelt = document.getElementById("title");
	if (titleelt != null)
	{
		SetStrapTitle(titleelt.innerHTML);
		titleelt.classList.add("hide");
	}
	
	var html_rhs_top = `
	<!-- Start of RightHandSide -->
	<DIV class="brick_column rhswidth" id="main_rhs">
` + ServicesBrick(prefix);

	var html_rhs_middle = `
		<DIV class="brick postcode nohover">
			<P class="strap">LOCAL PREDICTIONS</P>
			<H3>Postcode Lookup</H3>
			<P>Find your own seat, and see its predictions, ward-level mapping and demographics.</P>
			<P><B>Enter your postcode:</B></P>
			<FORM action="${prefix}fcgi-bin/seatdetails.py" id="form_postcode" onsubmit="return submit_postcode(this);">
				<DIV class="input_button">
					<INPUT type="text" name="postcode" class="fullwidth" maxlength="10"  
						placeholder="Postcode"><DIV class="button" onclick="form_go('form_postcode');">Go</DIV>
				</DIV>
				<DIV id="err_postcode" class="inputerror"></DIV>
			</FORM>
		</DIV> <!-- end of brick -->
		
		<DIV class="brick maps" onclick="gourl('${prefix}map_home.html');">
			<P class="strap">PREDICTION MAPS</P>
			<H3><A href="${prefix}map_home.html">Interactive Election Maps</A></H3>
			<P>Interactive maps available for both Equal Population and Geographical Predictions.</P>
			<A href="${prefix}map_home.html" class="onblue">View maps</A>
		</DIV> <!-- end of brick -->
		
		<DIV class="brick userpoll" onclick="gourl('${prefix}userpoll.html');">
			<P class="strap">USER-DEFINED POLL</P>
			<H3><A href="${prefix}userpoll.html">Make Your Prediction</A></H3>
			<P>Make your own predictions both for the entire country and for any particular Westminster constituency in
			England, Scotland and Wales.</P>
			<A href="${prefix}userpoll.html" class="onblue">Make your prediction</A>
		</DIV> <!-- end of brick -->
` + SubscribeBrick(prefix);

	var html_rhs_bottom = `
	</DIV> <!-- end of RHS brick_column -->
	`;
	
	var html_footer0 = `
<DIV class="footercontainer">
	<DIV class="footer0 flexrow" onclick="gourl('${prefix}services_together.html');">
		<DIV>
			<H3>We provide innovative and affordable MRP and consulting</H3>
			<P>Specialising in quantitative analysis and models for electoral and market
			research projects, discover how we can work together.</P>
		</DIV>
		<DIV><OBJECT data="${prefix}icon_fingers128.svg" type="image/svg+xml"
			onload="finger_init(this, '#80aa1bff', 168);"></OBJECT></DIV>
		<DIV class="button2">
				<A href="${prefix}services_together.html"><B>Let's work together</B></A>
		</DIV>
	</DIV>
</DIV>`;
	var html_footer12 = `
<DIV class="footercontainer">
	<DIV class="footer1">
		<DIV>
			<A href="${prefix}services_general.html"><H4>Services</H4></A>
			<P><A href="${prefix}services_polling.html">Polling Regression Analysis</A></P>
			<P><A href="${prefix}services_electoral.html">Election Predictions</A></P>
			<P><A href="${prefix}services_data.html">Electoral and Political Data</A></P>
			<P><A href="${prefix}services_solutions.html">Customised Maps &amp; solutions</A></P>
			<P><A href="${prefix}services_casestudy_ge2019.html">Case Studies</A></P>
		</DIV>
		<DIV>
			<A href="${prefix}prediction_home.html"><H4>UK Predictions</H4></A>
			<P><A href="${prefix}newseatlookup.html">Your Seat</A></P>
			<P><A href="${prefix}userpoll.html">Your Prediction</A></P>
			<P><A href="${prefix}prediction_main.html">Our prediction</A></p>
			<P><A href="${prefix}scotland.html">Scotland</A></P>
			<P><A href="${prefix}northernireland.html">Northern Ireland</A></P>
		</DIV>
		<DIV>
			<A href="${prefix}resources_home.html"><H4>UK Resources</H4></A>
			<P><A href="${prefix}boundaries2023.html">New Boundaries 2023</A></P>
			<P><A href="${prefix}map_home.html">Maps</A></P>
			<P><A href="${prefix}pol3d_main.html">3D Politics</A></P>
			<P><A href="${prefix}polls.html">Polls</A></P>
			<P><A href="${prefix}flatfile.html">Historical data</A></P>
		</DIV>
		<DIV>
			<H4><A href="${prefix}services_contact.html">Contact</A></H4>
			<P><B>Consultancy Contact:</B>
			<BR><SCRIPT>write_email("enquiry");</SCRIPT></P>
			<P><B>Media Contact:</B>
			<BR>Telephone: 020 3627 8141,
			<BR><SCRIPT>write_email("media");</SCRIPT></P>
			<BR>
			<DIV>
			<A href="https://twitter.com/ElectCalculus" target="_blank"><IMG src="${prefix}icon_twitter.svg"></A>
			&emsp;<A href="${prefix}rssfeed.rss"><IMG src="${prefix}icon_rss.svg"></A></DIV>
		</DIV>
		<DIV class="flexcol" id="gototop">
			<DIV onclick="gourl('#top');"><SVG width="44" height="44">
				<g transform="translate(22,22)">
				<CIRCLE cx="0" cy="0" r="20" id="gototop_circle" />
				<path d="M-7 2 L0 -5 L7 2" id="gototop_path" />
				</g>
			</SVG></DIV>
			<DIV><A href="#top">Back to top</A></DIV>
		</DIV>
	</DIV>
</DIV>
<DIV class="footercontainer">
	<DIV class="footer2">
		<DIV><P>Copyright ${year} Electoral Calculus Ltd. All rights reserved  |  
		<A href="${prefix}aboutus.html">About Us</A>  | 
		<A href="${prefix}terms_and_conds.html">Terms & Conditions</A>  |  
		<A href="${prefix}dataprivacy.html">Privacy Policy</A>
		<BR>
		<A href="https://designbull.co.uk/">Branding & UX by Designbull.co.uk</A></P>
		</DIV>
		<DIV class="flexrow">
			<DIV>POWERED BY </DIV>
			<DIV><IMG src="${prefix}TLLogo_medium_black.svg" alt="TigerLib"
				title="TigerLib" ></DIV>
		</DIV>
	</DIV>
</DIV> 
</DIV> <!-- wholepage -->
	`;
	
	document.write("</DIV> <!-- end of #main -->");
	if (!controllist.includes("hiderhs"))
	{
		document.write(html_rhs_top);
		if (!controllist.includes("toprhs")) { document.write(html_rhs_middle); }
		document.write(html_rhs_bottom);
	}
	else { document.getElementById("main").classList.add("wide"); }
	document.write("</DIV> <!-- end of main_outer -->");
	if (!controllist.includes("nofooter0")) { document.write(html_footer0); }
	document.write(html_footer12);
	CSInitAll();
	return;
}

// 2. FORM HANDLING ================================================

function ContactForm(prefix = "")
{
	var cf_html = `
<DIV class="brick nohover talkbox">
	<H3>Talk to an Electoral Calculus Expert</H3>
	<FORM action="${prefix}cgi-bin/salescontact.py" method=post name="salesform"
		onsubmit="return submit_contact(this);">
		<B>Name</B>
		<BR>
		<INPUT type="text" class="fullwidth" name="username" placeholder="Your name" maxlength=100>
		<DIV id="err_username" class="inputerror">&nbsp;</DIV>
		<B>Business email</B>
		<BR>
		<INPUT type="text" class="fullwidth" name="usermail" placeholder="email@org" maxlength=100>
		<DIV id="err_usermail" class="inputerror">&nbsp;</DIV>
		<B>Phone</B>
		<BR>
		<INPUT type="text" class="fullwidth" name="userphone" placeholder="Phone number" maxlength=30>
		<DIV id="err_userphone" class="inputerror">&nbsp;</DIV>
		<B>Company</B>
		<BR>
		<INPUT type="text" class="fullwidth" name="usercompany" placeholder="Company or organisation" maxlength=100>
		<DIV id="err_usercompany" class="inputerror">&nbsp;</DIV>
		<B>Your business goals</B>
		<BR>
		<textarea name="usergoals" class="usergoals" placeholder="What are you wanting to do" cols="" rows=""></textarea>
		<DIV id="err_usergoals" class="inputerror">&nbsp;</DIV>
		<INPUT type="submit" class="button fullwidth" value="Send">
	</FORM>
	<P class="smaller"><I>One of our experts will personally contact you</I></P>

</DIV>
`;
	document.write(cf_html);
}

// utility function to go to a URL when called
function gourl(url)
{
	window.location.href = url;
	return;
}
	
// Search functions
// utility function to submit a form
function form_go(formid)
{
	var elt = document.getElementById(formid);
	if (typeof elt.onsubmit === "function")
	{
		if (elt.onsubmit() == false) { return; }
	}
	elt.submit();
	return;
}

// subroutine of submit_postcode
function CheckPossiblePostcode(RawString)
{
	var pc_re = new RegExp("^([A-Za-z][A-Ha-hJ-Yj-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2})$");
	return pc_re.test(RawString);
}

// submit postcode form
function submit_postcode(elt)
{
	var pcode = elt.elements['postcode'].value;
	if (CheckPossiblePostcode(pcode) == false)
	{
		elt.querySelector("#err_postcode").innerHTML = "Please enter a postcode into this box";
		return false;
	}
	else
	{
		elt.querySelector("#err_postcode").innerHTML = "";
	}
	return true;
}

// function which does not submit form
function NoSubmit(event)
{
	if (event.keyCode == 13) 
	{
		event.preventDefault();
		return false;
	}
	return true;
}

// function to submit SubscribeForm
function SFSubmitForm(elt)
{
	var name = elt.username.value;
	var email = elt.address.value;
	var unsub_flag = (elt.subtype.value == "unsub");
	var name_re = new RegExp("(.{2,}) (.{2,})");
	var email_re = new RegExp(".+\@.+\..+");
	var ok_flag = true;
	if ((name_re.test(name) == false) && (unsub_flag == false))
	{
		elt.querySelector("#err_username").innerHTML = "Please enter your full (first and last) names to subscribe";
		ok_flag = false;
	}
	else
	{
		elt.querySelector("#err_username").innerHTML = "";
	}
	if (email_re.test(email) == false)
	{
		var verb = (unsub_flag ? "unsubscribe" : "subscribe");
		elt.querySelector("#err_address").innerHTML = "Please enter a valid email address to " + verb;
		ok_flag = false;
	}
	else
	{
		elt.querySelector("#err_address").innerHTML = "";
	}
	// blur all the buttons
	if (!ok_flag)
	{
		var sbuttons = elt.querySelectorAll('input[type="submit"]');
		for (var i =0;i<sbuttons.length;i++) { sbuttons[i].blur(); }
	}
	return ok_flag;
}

// subroutine of submit_contact
function submit_contact_check(elt, qname, errortext, isgood)
{
	if (isgood)
	{
		elt.querySelector("#err_" + qname).innerHTML = "&nbsp;";
		elt.elements[qname].classList.remove("invalid");
	}
	else
	{
		elt.querySelector("#err_" + qname).innerHTML = errortext;
		elt.elements[qname].classList.add("invalid");
	}
	return isgood;
}	

// submits ContactEnquiry form
function submit_contact(elt)
{
	var username = elt.elements['username'].value;
	var usermail = elt.elements['usermail'].value;
	var userphone = elt.elements['userphone'].value;
	var usercompany = elt.elements['usercompany'].value;
	var usergoals = elt.elements['usergoals'].value;
	var errorlist = new Array();
	
	var username_re = new RegExp("(.{2,})");
	var usermail_re = new RegExp(".+\@.+\..+");
	var userphone_re = new RegExp("([^0-9]*[0-9]){6}");
	var usercompany_re = new RegExp(".{6}");
	var usergoals_re = new RegExp(".");
	
	var ok_username = submit_contact_check(elt, "username", "Please enter your name", username_re.test(username));
	var ok_usermail = submit_contact_check(elt, "usermail", "Please enter your email", usermail_re.test(usermail));
	var ok_userphone = submit_contact_check(elt, "userphone", "Please enter your phone number", userphone_re.test(userphone));
	var ok_usercompany = submit_contact_check(elt, "usercompany", "Please enter your company/organisation", usercompany_re.test(usercompany));
	var ok_usergoals = submit_contact_check(elt, "usergoals", "Please enter your project goals", usergoals_re.test(usergoals));
	
	var ok_flag = ok_username && ok_usermail && ok_userphone && ok_usercompany && ok_usergoals;
	return ok_flag;
}

// function to write Radio button HTML
function RadioHTML(radioname, valuelist, labellist)
{
	var numitems = valuelist.length;
	if (labellist == null) { labellist = valuelist; }
	if (labellist.length != numitems) { window.alert("Internal error"); return; }
	textrows = new Array(numitems);
	for (var i=0;i<numitems;i++)
	{
		var itemid = radioname + "_" + ((i+1).toString().slice(-2));
		var inputtext = '<DIV><INPUT type="radio" name="' + radioname + '" id="' + itemid + '" value="' + valuelist[i] + '">\n';
		var labeltext = '<LABEL for="' + itemid + '">' + labellist[i] + '</LABEL></DIV>\n';
		textrows[i] = inputtext + labeltext; 
	}
	var totalhtml = textrows.join("");
	return totalhtml;
}


// 3. BRICK CODE ==================================

function BrickResizeItem(item){
	var grid = select_parent(item, ".masonry_container");
	//var grid = document.getElementsByClassName("masonry_container")[0];
	var rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
	var rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));
	var brickElt = item.querySelector(".brick");
	brickElt.style.height = "auto";
	var brickHeight = brickElt.getBoundingClientRect().height;
	var rowSize = Math.ceil(brickHeight/rowHeight);
	var adjHeight = rowHeight * rowSize;
	brickElt.style.height = adjHeight.toString() + "px";
	rowSpan = 1 + rowSize;
	item.style.gridRowEnd = "span " + rowSpan.toString();
	return;
}

function BrickResizeImage(evt)
{
	var imgelt = evt.currentTarget;
	var mb_elt = select_parent(imgelt, ".masonry_brick");
	if (mb_elt != null) { BrickResizeItem(mb_elt); }
	return;
}

function BrickResizeAllItems(){
	allItems = document.getElementsByClassName("masonry_brick");
	for(x=0;x<allItems.length;x++)
	{
		BrickResizeItem(allItems[x]);
	}
	allImages = document.querySelectorAll(".masonry_brick IMG");
	for (var i=0;i<allImages.length;i++)
	{
		if (!allImages[i].complete)
		{
			allImages[i].addEventListener('load', BrickResizeImage, false);
		}
	}
	return;
}



window.onload = BrickResizeAllItems;
window.onresize = BrickResizeAllItems;


// 4. CustomSelect and DropDown

// Gets parent of element which matches the selector (or null if not a descendant of any element which matches)
function select_parent(elt, selector)
{
	var thiselt = elt;
	while (thiselt.tagName != "BODY")
	{
		if (thiselt.matches(selector)) { return thiselt; }
		thiselt = thiselt.parentElement;
		if (thiselt == null)
		{
			return null;
		}
	}
	return null;
}

// CUSTOMSELECT ---------------------------------------



// Initialises all custom-select elements in the document
function CSInitAll()
{
	// Look for any elements with the class "custom-select"
	var cslist = document.getElementsByClassName("custom-select");
	
	// loop over custom-selects
	for (var i = 0; i < cslist.length; i++)
	{
		CSInit(cslist[i]);
	}
	return;
}

// Initialises this custom-select element (or a child)
function CSInit(selectelt)
{
	var cselt = select_parent(selectelt, ".custom-select");
	// give up if not a custom-select element
	if (!cselt.matches(".custom-select")) { return; }
	
	// get select element
	var selElmnt = cselt.getElementsByTagName("select")[0];
	var mult_flag = selElmnt.multiple;
	
	// remove any existing divs (in case of multiple calls)
	var existingdivs = cselt.querySelectorAll("div");
	for (var i=0;i<existingdivs.length;i++)
	{
		if (existingdivs[i].parentNode == cselt) { cselt.removeChild(existingdivs[i]); }
	}

	// For each custom-select, create a new DIV that will act as the selected item
	var adiv = document.createElement("DIV");
	adiv.classList.add("select-selected");
	if (mult_flag)
	{
		adiv.innerHTML = selElmnt[0].text;
		adiv.classList.add("placeholder");
	}
	else
	{
		if (selElmnt.selectedIndex == 0)
			{ adiv.classList.add("placeholder"); }
		adiv.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
	}
	cselt.appendChild(adiv);
	
	if (selElmnt.required) { adiv.classList.add("required"); }
	if (selElmnt.disabled)
	{
		adiv.classList.add("disabled");
		return;
	}
	// For each custom-select, create a new DIV that will contain the option list:
	var bdiv = document.createElement("DIV");
	bdiv.setAttribute("class", "select-items select-hide");
	if (mult_flag)
	{
		bdiv.classList.add("multiple");
	}
	for (var j = 1; j < selElmnt.length; j++)
	{
		// For each option in the original select element,
		// create a new DIV that will act as an option item
		var cdiv = document.createElement("DIV");
		cdiv.innerHTML = selElmnt.options[j].innerHTML;
		if (selElmnt[j].selected) { cdiv.classList.add("same-as-selected"); }
		cdiv.addEventListener("click", function(evt) {
			// When an item is clicked, update the original select box,	and the selected item
			var selelt = this.parentNode.parentNode.getElementsByTagName("select")[0];
			var mult_flag = selelt.multiple;
			var aelt = this.parentNode.previousSibling;
			// skip the first option because it is the placeholder
			for (var k = 1; k < selelt.length; k++)
			{
				if (selelt.options[k].innerHTML == this.innerHTML)
				{
					if (mult_flag) { CSToggleSelect(this, k); }
						else { CSSetIndex(aelt.parentNode, k); }
					break;
				}
			}
			selElmnt.dispatchEvent(new Event('change', {bubbles:true}));
			if (!mult_flag) { aelt.click(); }
		});
		bdiv.appendChild(cdiv);
	}
	cselt.appendChild(bdiv);
	adiv.addEventListener("click", function(evt) {
		// When the select box is clicked, close any other select boxes,
		// and open/close the current select box
		evt.stopPropagation();
		CS_CloseAll(this);
		this.nextSibling.classList.toggle("select-hide");
		this.classList.toggle("select-arrow-active");
	});
	return;
}


// sets index on custom-select
// input elemnt can be DIV.custom-select or any child
function CSSetIndex(elemnt, index)
{
	var cselt = select_parent(elemnt, ".custom-select");
	var selElmnt = cselt.getElementsByTagName("select")[0];
	// set index on SELECT itself
	selElmnt.selectedIndex = index;
	
	// update DIV structure
	// firstly update DIV.select-selected
	var aelt = cselt.querySelector(".select-selected");
	aelt.innerHTML = selElmnt.options[index].text;
	if (index > 0) { aelt.classList.remove("placeholder"); }
		else { aelt.classList.add("placeholder"); }
	// secondly update all the DIVs inside DIV.select-items
	var celts = cselt.querySelectorAll(".select-items > div");
	for (var ll=0;ll<celts.length;ll++)
	{
		if (ll+1 == index) { celts[ll].classList.add("same-as-selected"); }
			else { celts[ll].classList.remove("same-as-selected"); }
	}
	return;
}

// toggles selection of multiple select item
function CSToggleSelect(elemnt, index)
{
	var cselt = select_parent(elemnt, ".custom-select");
	var selElmnt = cselt.getElementsByTagName("select")[0];
	
	var newvalue = !selElmnt[index].selected;
	// set index on OPTION element
	selElmnt[index].selected = newvalue;
	
	var numselected = selElmnt.selectedOptions.length;
	// update DIV structure
	// firstly update DIV.select-selected
	var aelt = cselt.querySelector(".select-selected");
	var astring = selElmnt[0].text;
	if (numselected > 0) { astring = numselected.toString() + " item(s) selected"; }
	aelt.innerHTML = astring;
	if (numselected > 0) { aelt.classList.remove("placeholder"); }
		else { aelt.classList.add("placeholder"); }
	// secondly update all the DIVs inside DIV.select-items
	var celts = cselt.querySelectorAll(".select-items > div");
	for (var ll=0;ll<celts.length;ll++)
	{
		if (selElmnt[ll+1].selected) { celts[ll].classList.add("same-as-selected"); }
			else { celts[ll].classList.remove("same-as-selected"); }
	}
	return;
}


// selects item in custom-select by defining the value
// input elemnt can be DIV.custom-select or any child
function CSSetValue(elemnt, value)
{
	var cselt = select_parent(elemnt, ".custom-select");
	var selElmnt = cselt.getElementsByTagName("select")[0];
	for (var k = selElmnt.length-1; k>=0;k--)
	{
		if (value == selElmnt.options[k].value)
		{
			CSSetIndex(cselt, k);
			break;
		}
	}
	return;
}

// A function that will close all select boxes in the document,
// except the current select box
function CS_CloseAll(elmnt)
{
	// get parent custom-select element
	var cselt = select_parent(elmnt, ".custom-select");
	// get list of all custom-select elements
	var cslist = document.getElementsByClassName("custom-select");
	for (var i = 0; i < cslist.length; i++)
	{
		if (cselt != cslist[i])
		{
			var sselt = cslist[i].querySelector(".select-selected");
			if (sselt == null) { continue; }
			sselt.classList.remove("select-arrow-active");
			var sielt = sselt.nextElementSibling;
			if (sielt != null) { sielt.classList.add("select-hide"); }
		}
	}
	return;
}


// DROPDOWN -------------------------------------

// Gets DropDown parent for element (or null if not a descendant of any DropDown)
function dd_parent(elt)
{
	return select_parent(elt, ".dropdown");
}

function dd_state(elt)
{
	var state = (elt.classList.contains("show") ? 1 : 0) + (elt.classList.contains("sticky") ? 1 : 0);
	return state;
}

/* DropDown : when the user clicks on the button,
	toggle between hiding and showing the dropdown content */
function dd_click(evt) {
	var elt = evt.target;
	var ddelt = dd_parent(elt);
	if (ddelt == null) { return; }
	
	var currstate = dd_state(ddelt);
	var newstate;
	if (evt.type == "click")
	{
		newstate = (currstate == 0 ? 2 : 0);
	}
	else if ((evt.type == "mouseon" ) || (evt.type == "mouseover"))
	{
		newstate = Math.max(currstate, 1);
	}
	else if (evt.type == "mouseout")
	{
		newstate = (currstate == 2 ? 2 : 0);
	}
	if (newstate == currstate) { return; }
	if (newstate == 0) { ddelt.classList.remove("show", "sticky"); return; }
	
	// hide all dropdown menus, in case some others are visible, as long as they are not bigger than newstate
	var okflag = dd_hide_all(newstate);
	if (!okflag) { return; }
	ddelt.classList.add("show");
	if (newstate == 2) { ddelt.classList.add("sticky"); }
	return;
}

// hide all dropdown menus. Returns true if successful, or false if more important dropdown open
function dd_hide_all(statethresh)
{
	var dropdowns = document.getElementsByClassName("dropdown");
	var maxstate = -1;
	for (var i = 0; i < dropdowns.length; i++)
	{
		maxstate = Math.max(maxstate, dd_state(dropdowns[i]));
	}
	if (maxstate > statethresh) { return false; }
	for (var i = 0; i < dropdowns.length; i++)
	{
		dropdowns[i].classList.remove("show", "sticky");
	}
	return true;
}

// run if any click made on the page
// if outside a DropDown area, then close all DropDown ULs
function dd_check_click(elt)
{
	if (dd_parent(elt) == null)
	{
		dd_hide_all(2);
	}
}


// Check with all clickable classes to see if they need to close
window.onclick = function(event)
{
	CS_CloseAll(event.target);
	dd_check_click(event.target);
	return;
}

// 5. UTILITIES

// debug utility to write log messages to new window
function log(message)
{
	if (!log.window_ || log.window_.closed) 
	{
		var win = window.open("", null, "width=400,height=200," +
							  "scrollbars=yes,resizable=yes,status=no," +
							  "location=no,menubar=no,toolbar=no");
		if (!win) return;
		var doc = win.document;
		doc.write("<html><head><title>Debug Log</title></head>" +
				  "<body></body></html>");
		doc.close();
		log.window_ = win;
	}
	var logLine = log.window_.document.createElement("div");
	logLine.appendChild(log.window_.document.createTextNode(message));
	log.window_.document.body.appendChild(logLine);
}

// utility to write email address to web page
function write_email(emailid)
{
	var email_addr = emailid + String.fromCharCode(64) + "electoralcalculus.co.uk";
	var outstring = '<A href="mailto:' + email_addr + '">' + email_addr + '</A>';
	document.write(outstring);
	return;
}

// Function to initialise finger icon (by changing colour and size)
// colour can be 4-bytes with opacity as the highest byte (00=transparent, ff=opaque)
function finger_init(elt, colour, width)
{
	var svgdoc = elt.contentDocument;
	var svgelt = svgdoc.getElementById("svgelt");
	if (width > 0)
	{
		var oldwidth = parseInt(svgelt.getAttribute('width'), 10);
		var oldheight = parseInt(svgelt.getAttribute('height'), 10);
		var scale = width / oldwidth;
		svgelt.setAttribute('width', width.toString() + 'px');
		var height = oldheight * scale;
		svgelt.setAttribute('height', height.toString() + 'px');
	}
	var fingerelt = svgdoc.getElementById("fingers");
	if (colour.match("#[0-9A-Fa-f]{8}"))
	{
		var opacity = parseInt(colour.substring(1,3), 16) / 255.0;
		var purecolour = "#" + colour.substring(3, 9);
		fingerelt.style.fillOpacity = opacity;
		fingerelt.style.fill = purecolour;
	}
	else if (colour != null) {	fingerelt.style.fill = colour; }
	return;
}

function testimonial_logos()
{
	var html=`
	<P>Recent clients and partners include</P>
<DIV class="testi">
	<DIV> <!-- first row -->
		<IMG src="testi_constsoc.png"><IMG src="testi_savanta.png" class="lighten"><IMG src="testi_jlp.png" class="lighten">
	</DIV>
	<DIV> <!-- second row -->
		<IMG src="testi_fon.png"><IMG src="testi_propchron.png" class="large">
	</DIV>
</DIV>
<P>Electoral Calculus is a member of the British Polling Council and abides by its rules.</P>
`;
	document.write(html);
	return;
}


// Routine to create on-the-fly styles for a table to control the text-align of each column
// Usage Example: (format a four-column table: Left, Right, Right, Center
// <SCRIPT>TableColumnFormat("lrrc")</SCRIPT>         <!-- create a class called .lrrc -->
// <TABLE border=1 class=lrrc>                        <!-- class name must match JS call -->
// ...
function TableColumnFormat(template)
	{
		document.write('<style type="text/css">\n');
		var ncols = template.length;
		var i, j;
		for (i=0; i<ncols; i++)
		{
			var stylestring = 'table.' + template + ' td:first-child ';
			for (j=0;j<i;j++)
			{
				stylestring = stylestring + '+ td ';
			}
			stylestring = stylestring + '{ text-align: ';
			var thischar = template.charAt(i);
			var alignstr = 'none';
			if (thischar == 'l')
				alignstr = 'left';
			if (thischar == 'c')
				alignstr = 'center';
			if (thischar == 'r')
				alignstr = 'right';
			stylestring = stylestring + alignstr + '; }\n';
			document.write(stylestring);
			var th_string = stylestring.replace(/td/g, "th");
			document.write(th_string);
		}
		document.write('</style>');
		return;
	}

// Routine for ConList pages to give Safe/Unsafe status for each seat
function safe_seat(safeflag, winners, prefix="")
{
	if (safeflag == true)
	{
		document.write('<TR><TD colspan=5 Align=Left><IMG src="' + prefix + 'safe.gif" align=top>&nbsp;<A href="safeseat.html?win=' + winners + '">This seat is <B>Safe</B></A> ');
		document.write('and voters have little say on their MP</TR>');
	}
	if (safeflag == false)
	{
		document.write('<TR><TD colspan=5 Align=Left><IMG src="' + prefix + 'unsafe.gif" align=top>&nbsp;<A href="unsafeseat.html?win=' + winners + '">This seat is not safe</A> ');
		document.write('and voters have a real say on their MP</TR>');
	}
	return;
}

// showclass can either be a class name which will be toggles on element (to help styling)
// or a combo like ".parentclass:toggleclass", which will toggle toggleclass in the parent
// with matching parentclass
function ShowHideDiv(element, divname, showtext = "Show", hidetext = "Hide", showclass = "")
{
	var oldstate = document.getElementById(divname).className;
	var showelt = null;
	var sclass = null;
	if (showclass != "")
	{
		var tokens = showclass.split(":");
		if (tokens.length > 1)
		{
			showelt = select_parent(element, tokens[0]);
			sclass = tokens[1];
		}
		else
		{
			showelt = element;
			sclass = showclass;
		}
	}
	if (oldstate == "ShowHide_Hide")
	{
		document.getElementById(divname).className = "ShowHide_Show";
		element.innerHTML = hidetext;
		if (showelt != null) { showelt.classList.add(sclass); }
	}
	else
	{
		document.getElementById(divname).className = "ShowHide_Hide";
		element.innerHTML = showtext;
		if (showelt != null) { showelt.classList.remove(sclass); }
	}
	element.blur();
	return;
}

// version for NavMobile, which closes all other kct_toggle divs
function ShowHideDivNM(element, divname)
{
	// close all other toggles
	var myaccordion = select_parent(element, ".nm_accordion");
	var allaccordia = document.querySelectorAll(".nm_accordion");
	for (var i=0;i<allaccordia.length;i++)
	{
		if (myaccordion == allaccordia[i]) { continue; }
		var thistoggle = allaccordia[i].querySelector(".kct_toggle");
		if (thistoggle.classList.contains("show"))
		{
			var thisclicker = thistoggle.querySelectorAll("div")[1];
			var thistarget = allaccordia[i].querySelectorAll(":scope > div")[1];
			ShowHideDiv(thisclicker, thistarget.id, "&emsp;", "&emsp;", ".kct_toggle:show");
		}
	}
	ShowHideDiv(element, divname, "&emsp;", "&emsp;", ".kct_toggle:show");
	return;
}

// function which converts an integer value like 0xff00cc into a seven-character hex string '#ff00cc'
function hexstring(value)
{
    var hstring = '#' + (value + 0x1000000).toString(16).substr(-6)
    return hstring;
}

// converts coded colour string, such as "R02B05" and newflag into HTML colour such as "#2020FF"
// This routine is coded in three places.
// 1. C++ : decode_colour in election.cpp, used by xl_MapSVGFileWrite
// 2. JavaScript : SqColour in dmap_routines.js, used by Dynamic Map web pages
// 3. PostScript : setcolour in equalmap_2015.ps, used for A1 poster
// newflag = 0 (last general election), 1 (predicted result), 2 (changed seats) 
// R = red (#ff0000), B = blue (#0000ff), G = green (#00ff00), Y = yellow (#ffff00), O = orange (#ff9900)
// P = purple (#c700c7), V = green (#00ff00), Z = grey (#404040), C = cyan (#00ffff), X = brown (#cc6600)
function SqColour(colcode, newflag)
{
	var colstr;
	if ((newflag == 0) || (newflag == 1))
		colstr = colcode.substr(newflag==1 ? 3 : 0, 3);
	else if (colcode.charAt(0) != colcode.charAt(3))
		colstr = colcode.substr(3, 3);
	else
		colstr = "Z00";
	var colour = colstr.substr(0,1);
	
	var minsat = 100.0/255.0;
	var lambda = Math.min(1.0, Number(colstr.substr(1,2))/40.0);
	var saturation = minsat + lambda*(1.0-minsat);
	var red = 0.0;
	var green  = 0.0;
	var blue = 0.0;
	if (colour == 'R') { red = 1.0; }
	else if (colour == 'G') { green = 1.0; }
	else if (colour == 'B') { blue = 1.0; }
	else if (colour == 'Y') { red = 1.0; green = 1.0; }
	else if (colour == 'O') { red = 1.0; green = 0.6; }
	else if (colour == 'P') { red = 0.78; blue = 0.78; }
	else if (colour == 'V') { green = 1.0; }
	else if (colour == 'Z') { red = 0.25; green = 0.25; blue = 0.25; }
    else if (colour == 'C') { red = 0.0; green = 1.0; blue = 1.0; }
    else if (colour == 'X') { red = 0.8; green = 0.4; blue = 0.0; }
	
	red = Math.round(255*(1.0 - saturation * (1.0 - red)));
	green = Math.round(255*(1.0 - saturation * (1.0 - green)));
	blue = Math.round(255*(1.0 - saturation * (1.0 - blue)));
	
	red = (red < 16 ? '0' : '') + red.toString(16);
	green = (green < 16 ? '0' : '') + green.toString(16);
	blue = (blue < 16 ? '0' : '') + blue.toString(16);
	var htmlcol = '#' + red + green + blue;
	return htmlcol;
}



// can take either AreaCode or AreaName as input
// used by openseatmap.html
        
var AreaNames = new Array("Null", "Northern Ireland", "Scotland", "North East", "North West", "Yorks/Humber",
	"Wales", "West Midlands", "East Midlands", "Anglia", "South West", "London", "South East");
    
function PartyNameShow2(Party, Area)
{
    var areaname = Area;
    if (!isNaN(Area))
        areaname = AreaNames[Area];
    if (Party == 'NAT')
	{
		if (areaname == "Scotland")	{ return 'SNP';	}
		if (areaname == "Northern Ireland") { return 'SF'; }
		if (areaname == "Wales") {	return 'Plaid';	}
	}
	if (areaname == "Northern Ireland")
	{
		if (Party == 'CON') { return 'UUP'; }
		if (Party == 'LAB') { return 'SDLP'; }
		if (Party == 'LIB') { return 'DUP'; }
        if ((Party == 'Reform') || (Party == 'Brexit')) { return 'Alliance'; }
	}
	return Party;
}




// 6. GENERAL DATALOAD FUNCTIONS
//
// To use these is quite simple
// In the JavaScript have a line like
// <SCRIPT>var SeatData = new Array; DataLoadStart(SeatData, "electdata_2015.txt", MyFunc)</SCRIPT>
// When the data is loaded, it will run the function MyFunc().
// The data will be visible in the array SeatData, which is an array of objects, each object indexed
// by the header row of the data, eg SeatData[0]["Name"] is the name of the first seat.
// Can also use URLs like "cgi-bin/dataserver.py?type=googleseat" to get custom data reports
//

function DataLoadStart(ArrayToUse, URLaddress, FunctionToCall, PostData)
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.tiger_loadeddata = ArrayToUse;	// shallow copy
	xmlhttp.tiger_loadedfunction = FunctionToCall;
	xmlhttp.onreadystatechange = function() { DataLoadEnd(xmlhttp); };
    if (typeof PostData == "undefined")
    {
        xmlhttp.open("GET", URLaddress, true);
        xmlhttp.send();
    }
    else
    {
        xmlhttp.open("POST", URLaddress, true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.send(PostData);
    }	
	return;
}


function DataLoadEnd(httprequest)
{
	if ((httprequest.readyState != 4) || (httprequest.status != 200))
		return;
    if (!httprequest.hasOwnProperty('tiger_loadedfunction'))
        return;
		
	var datafile = httprequest.responseText;
	var datalines = datafile.replace(/[\r]/g, '').split("\n");
	var header = datalines[0].split(String.fromCharCode(30));
	var numrows = datalines.length - 2;
	var numcols = header.length;
	httprequest.tiger_loadeddata.length = numrows;
    // Messy regular expression to cope with exponential notation as well
	var NumRegex = new RegExp("^[\+-]?[0-9]+\.?[0-9]*(e[\+-]?[0-9]+)?$")
	for (var i=0; i<numrows; i++)
	{
		var thisobject = new Object;
		var thisline = datalines[i+1].split(String.fromCharCode(30));
		for (var j=0; j<numcols; j++)
		{
			var value = thisline[j];
			if (NumRegex.test(value)) value = Number(value);
			thisobject[header[j]] = value;
		}
		httprequest.tiger_loadeddata[i] = thisobject;
	}
	httprequest.tiger_loadedfunction();
	return;
}

// END OF GENERAL DATALOAD FUNCTIONS



// 7. GEOSERVER ROUTINES

function getGeoServerDetails()
{
    var Details = {};
    var thisurl = window.location.href;
    var baseurl = 'https://www.electoralcalculus.co.uk/geoserver/';
    var signal = '';
    // Test locations - for ElectoralCalculus use only
    if (thisurl.substring(0,17) == "http://localhost/")
    {
        baseurl = 'http://localhost/geoserver/';
        signal = 'localhost';
    }
    else if (thisurl.lastIndexOf("http://192.168.1.129/", 0) === 0)
    {
        baseurl = 'http://192.168.1.129/geoserver/';
        signal = 'darkbox';
    }
    else if (thisurl.substring(0,40) == "https://wsl.electoralcalculus.co.uk:444/")
    {
        baseurl = 'https://wsl.electoralcalculus.co.uk:444/geoserver/';
        signal = 'wsl';
    }
    else if (thisurl.substring(0,20) == "http://localhost:83/")
    {
        baseurl = 'http://localhost/geoserver/';
        signal = 'dev';
    }
	else if (thisurl.substring(0,37) == "https://wsl2.electoralcalculus.co.uk/")
    {
        baseurl = 'https://wsl2.electoralcalculus.co.uk/geoserver/';
        signal = 'wsl2';
    }
	else if (thisurl.substring(0,37) == "https://t203.electoralcalculus.co.uk/")
    {
        baseurl = 'https://t203.electoralcalculus.co.uk/geoserver/';
        signal = 't203';
    }
    Details.baseurl = baseurl;
    Details.signal = signal;
    return Details;
}

function cql_escape(instring)
{
    var outstring = instring.replace("'", "''");
    return outstring;
}

// fixes the "zoom-out" button is jsopenlayers, which is in UTF-8
function FixZoomOut(mapid)
{
	document.getElementById(mapid).querySelector(".ol-zoom-out").innerHTML = "&minus;";
	return;
}

// END OF GEOSERVER ROUTINES



