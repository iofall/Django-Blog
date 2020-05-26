document.querySelector('body').onload= function() {myFunctionImgDetail()};

function myFunctionImgDetail() {
  myFunctionImgEdit()
  for (var element of document.querySelectorAll(".card-body img")) {
    element.classList.add('img-fluid', 'rounded');
  }
}

var body = document.querySelector('.editable');

document.querySelector('body').onclick= function() {myFunctionImgEdit()};

function myFunctionImgEdit() {
  for (var element of document.querySelectorAll(".editable img")) {
    element.classList.add('img-fluid', 'rounded');
  }
}
