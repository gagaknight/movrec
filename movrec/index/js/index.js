$('#sign-up-btn').click(function()
		{
		window.location.replace('../register');
		});
$('#sign-in-btn').click(function() 
		{
		$.ajax({
url:'../login_user',
data:{username:$('#username').val(),password:$('#password').val()}
}).done(function( msg ) {
	if(msg=="Success")
	{
	alert('Login Successful');
	location.reload();
	}
	else
	{
	alert('Login Failed');
	}
	});
		});
$('#get-rated-movies').click(function() 
		{
		$('#recommended-movies').html("");
		userId = $('#uid').val();
		$.ajax({
url:'../get_rated_movies',
data:{userId:userId}
}).done(function( msg ) {
	for (i=0;i<msg.length;i++)
	{
	$('#rated-movies').append('<div>' + msg[i]['title'] + '</div><br><div id="rated-movie-rated-bar-' + i + '"></div><br>');
	$('#rated-movies').append('<hr>');
	$('#rated-movie-rated-bar-'+i).rateYo({starWidth: "30px",readOnly:true,rating:msg[i]['rating']});
	}
	});
		});
$('#get-recommended-movies').click(function() 
		{
		$('#rated-movies').html("");
		$('#recommended-movies').html("");
		userId = $('#uid').val();
		$.ajax({
url:'../get_recommended_movies',
data:{userId:userId}
}).done(function( msg ) {
	for (i=0;i<msg.length;i++)
	{
	$('#recommended-movies').append("<span id='rec-title-" + i + "'>" + msg[i]['title'] + '</span><input type="hidden" id="mId-' + i + '"  value="'+msg[i]['movieId']+'">');
	$('#recommended-movies').append("<div id='rating-bar-"+i+"'></div>");
	$('#recommended-movies').append("<button id='rate-btn-" + i + "'>Rate this movie</button>");
	$('#rating-bar-'+i).rateYo({starWidth: "30px",fullStar:true});
	$('#recommended-movies').append('<hr>');
	$('#rate-btn-'+i).click(function() 
		{
		var btn_id = this.id.split("-");
		var movieId = $('#mId-'+btn_id[2]).val();
		var $rateYo = $('#rating-bar-'+btn_id[2]).rateYo();
		var rating = $rateYo.rateYo("rating");
		var userId = $('#uid').val();
		var index = btn_id[2];
		$.ajax({
url:'../rate_movie',
data:{userId:userId, movieId:movieId,rating:rating}
});
		$rateYo.hide();
		$('#rate-btn-'+index).next().hide();//hr tag
		$('#rec-title-'+index).hide();
		$('#rate-btn-'+index).hide();
		});
}
setInterval(check_recommended_movies, 10000);
});
});
/*if not log in*/
if( $('#highest-avg-rating-movies').length )
{
	$.ajax({
url:'../get_highest_avg_rating/',
}).done(function( msg ) {
	for (i=0;i<msg.length;i++)
	{
	$('#highest-avg-rating-movies').append('<span>' + msg[i]['title'] + '</span><br><div id="highest-avg-movie-rated-bar-' + i + '"></div><br>');
	$('#highest-avg-rating-movies').append('<hr>');
	$('#highest-avg-movie-rated-bar-'+i).rateYo({starWidth: "30px",rating:msg[i]['avg_rating']});
	}
	});
}
function check_recommended_movies()
{
	userId = $('#uid').val();
	$.ajax({
url:'../get_recommended_movies',
data:{userId:userId}
}).done(function( msg ) {
	for (i=0;i<msg.length;i++)
	{
	//check if title matches
	title = $('#rec-title-'+i).text();
	//alert(msg[i]['title'] + "\n" + title);
	if(title.trim()!=msg[i]['title'].trim())
	{
	$('#rec-title-'+i).text(msg[i]['title']);
	$('#mId-'+i).val(msg[i]['movieId']);
	/*show div*/
	var $rateYo = $('#rating-bar-'+ i).rateYo();
	$rateYo.rateYo("rating",0);
	$rateYo.show();
	$('#rate-btn-'+i).next().show();//hr tag
	$('#rec-title-'+i).show();
	$('#rate-btn-'+i).show();
	}
	}
	});
}
