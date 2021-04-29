var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID', productID, 'Action', action)

        console.log('USER', user)
        if(user === 'AnonymousUser'){
            addCookieItem(productID, action)
        }else{
            updateUserOrder(productID, action)
        }
    })
}


function addCookieItem(productID, action){
    
    if(action == 'add'){
        if(cart[productID] == undefined){
            cart[productID] = {'quantity':1}
        }else{
            cart[productID]['quantity'] += 1
            console.log("added")
        }
    }

    if(action == 'remove'){
        cart[productID]['quantity'] -= 1
        if(cart[productID]['quantity'] <= 0){
            console.log("removed")
            delete cart[productID]
        }
    }
    console.log(cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
}




function updateUserOrder(productID, action){

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        location.reload()
    });

}

