
var widthinfo = window.innerHeight;

var card = document.getElementById('cards');

var cardArray = Array.prototype.slice.call(card);

var cardbtn = document.getElementById('cartbtn');

var cartdArr = Array.prototype.slice.call(cardbtn);


cardArray.forEach(function (topi) { // Now itterate over each image in the array
    if (widthinfo <= 765) { // If the width is less than 50
        // Set the height and width
        topi.style.setAttribute('width', '100%');
    }
});

cartdArr.forEach(function (btn) { // Now itterate over each image in the array
    if (widthinfo <= 765) { // If the width is less than 50
        // Set the height and width
        btn.style.setAttribute('background-color', 'red');
    }
});

//$('#cards').width('100%')



// if (widthinfo < 765) {
//     card.style.width = '100%';
// }
// else {
//     card.style.width = '18rem'
// }




