function htadd(data) {
    var ht='';
    ht+=' <div class="first">';
	ht+='<div class="news_content"><div class="img_left">';
	if (data.news_image1.indexOf('http')===-1){
	    var imgUrl = data.news_image1.split('/');
        imgUrl.shift();
        imgUrl.shift();
        var ImgUrls = imgUrl.join('/');
        ht+='<img src="/static/' + ImgUrls + '"/></div><div class="con_right">';
    }else {
	    ht+='<img src="' + data.news_image1 + '"/></div><div class="con_right">';
    }

	ht+='<a class="tit" href="/newsdetail/" onclick="detailNav(' + data.id + ')">' + data.news_title + '</a>';
	ht+='<div class="con"><a href="/newsdetail/" onclick="detailNav(' + data.id + ')">' + data.news_content + '</a></div></div></div></div>';
	return ht;
}
function imgSize() {
    var oNews = document.getElementsByClassName('news_')[0];
    imgs = oNews.getElementsByTagName('img');
    for(var i=0; i<imgs.length; i++){
        if (imgs[i].clientHeight>imgs[i].clientWidth){
            imgs[i].style.height='100%';
        }else {
            imgs[i].style.width='100%';
        }
    }
}
function detailNav(newsId) {
    localStorage.setItem('newsId', ''+newsId);
}