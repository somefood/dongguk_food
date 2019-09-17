$(function(){
	var checkN1 = 0;
	var checkN2 = 0;
	var checkN3 = 0;
	var checkN4 = 0;
	if($("input:checkbox[id='agree1_button']").is(":checked")==true){
		$(".agree1_label").css({"background-image":"url('/static/img/button2.png')"});
	}
	if($("input:checkbox[id='agree2_button']").is(":checked")==true){
		$(".agree2_label").css({"background-image":"url('/static/img/button2.png')"});
	}
	if($("input:checkbox[id='agree3_button']").is(":checked")==true){
		$(".agree3_label").css({"background-image":"url('/static/img/button2.png')"});
	}
	$(".agree1_label").click(function(){
		if(checkN1==0){
			$(this).css({"background-image":"url('/static/img/button2.png')"});
			checkN1=1;
		}else{
			$(this).css({"background-image":"url('/static/img/button1.png')"});
			checkN1=0;
			checkN4=0;
			$(".agree4_label").css({"background-image":"url('/static/img/button1.png')"});
		}
	});
	$(".agree2_label").click(function(){
		if(checkN2==0){
			$(this).css({"background-image":"url('/static/img/button2.png')"});
			checkN2=1;
		}else{
			$(this).css({"background-image":"url('/static/img/button1.png')"});
			checkN2=0;
			checkN4=0;
			$(".agree4_label").css({"background-image":"url('/static/img/button1.png')"});
		}
	});
	$(".agree3_label").click(function(){
		if(checkN3==0){
			$(this).css({"background-image":"url('/static/img/button2.png')"});
			checkN3=1;
		}else{
			$(this).css({"background-image":"url('/static/img/button1.png')"});
			checkN3=0;
			checkN4=0;
			$(".agree4_label").css({"background-image":"url('/static/img/button1.png')"});
		}
	});
	$(".agree4_label").click(function(){
		if(checkN4==0){
			$(".agree1_label").css({"background-image":"url('/static/img/button2.png')"});
			$(".agree1_label").css({"background-image":"url('/static/img/button2.png')"});
			$(".agree2_label").css({"background-image":"url('/static/img/button2.png')"});
			$(".agree3_label").css({"background-image":"url('/static/img/button2.png')"});
			$(".agree4_label").css({"background-image":"url('/static/img/button2.png')"});
			checkN1=1;
			checkN2=1;
			checkN3=1;
			checkN4=1;
			$("#agree1_button").prop("checked", true);
			$("#agree2_button").prop("checked", true);
			$("#agree3_button").prop("checked", true);
		}else{
			$(".agree1_label").css({"background-image":"url('/static/img/button1.png')"});
			$(".agree2_label").css({"background-image":"url('/static/img/button1.png')"});
			$(".agree3_label").css({"background-image":"url('/static/img/button1.png')"});
			$(".agree4_label").css({"background-image":"url('/static/img/button1.png')"});
			checkN1=0;
			checkN2=0;
			checkN3=0;
			checkN4=0;
			$("#agree1_button").prop("checked", false);
			$("#agree2_button").prop("checked", false);
			$("#agree3_button").prop("checked", false);
		}
	});
	$(".nextButton").click(function(){
		if($("input:checkbox[id='agree1_button']").is(":checked")==true){
			if($("input:checkbox[id='agree2_button']").is(":checked")==true){
				location.href='/accounts/signup?type=1';
			}else{
				alert('개인정보 활용에 동의 부탁드립니다.');
			}
		}else{
			alert('이용약관에 동의 부탁드립니다.');
		}
	});
});