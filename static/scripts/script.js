// NAVBAR VARIABLES
var nav = $('nav');
var page = $(window);
var navItem = $('.nav-item');
var navLink = $('a.nav-link');
var navLogo = $('.navbar-logo')
var navLogoImg = $('.navbar-logo-img')

// NAVBAR SCROLL FUNCTION
page.scroll(function(){
    if (page.scrollTop() > 199) 
    {
        nav.addClass('bg-dark');
        navLink.css('color', 'white');
        navItem.css('margin-top', '0px');
        navLogo.css('margin-top', '0px');
        navLogoImg.css('filter', 'invert(1)');
    }
    else 
    {
        nav.removeClass('bg-dark');
        navLink.css('color', 'black');
        navItem.css('margin-top', '40px');
        navLogo.css('margin-top', '40px');
        navLogoImg.css('filter', 'invert(0)');
    }
});

// MAIN CONTENT VARIABLES
var tdHeaderParagraph = $('p.td-header-paragraph');
var tdHeaderHeader = $('p.td-header-header');

// MAIN CONTENT SCROLL FUNCTION
page.scroll(function() {
    if (page.scrollTop() < 199)
    {
        tdHeaderParagraph.css('opacity', '0');
        tdHeaderHeader.css('opacity', '0');
    }
    if (page.scrollTop() > 280)
    {
        tdHeaderParagraph.css('opacity', '1');
    }
    if (page.scrollTop() > 180) 
    {
        tdHeaderHeader.css('opacity', '1');
    }
});