var header = document.getElementById('header');
var content = document.querySelector('.content');
window.onscroll = function () {
    var scrolltop = document.documentElement.scrollTop || document.body.scrollTop;
    if(scrolltop > 20){
        header.style.opacity = 0.8;
    }else {
        header.style.opacity = 1;
        header.style.transition = 'opacity 0.3s ease';
    }
}
