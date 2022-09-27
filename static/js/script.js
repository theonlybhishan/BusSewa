
$(document).ready(function(){
    $("#sld").datepicker({
        minDate: 0,
        maxDate: 3,
    });
});


// seat selectiion section
var busId
var busName
var busPrice
var busuniqueid
const container = document.querySelector('.select-container');
const seats = document.querySelectorAll('.seat-row .seat:not(.occupied)');
const reward= document.getElementById('reward');
const count= document.getElementById('count');
const total = document.getElementById('total');
const price = document.getElementById('fare');
// const amountbtn = document.getElementById('book-btn');
// console.log(amountbtn.value);
// let ticketPrice = +price.value;
console.log(busPrice)
// let ticketPrice = busPrice
// console.log('ticketPrice',ticketPrice)
// const ticketPrice = ticketPrice;
// console.log(ticketPrice);
const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
// console.log('selectedSeats:',selectedSeats)



// update total and count
function updateSelectedCount(){
    const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
    const seatsIndex = [...selectedSeats].map(function(seat){
        return[...seats].indexOf(seat);
    });
    localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));
    // console.log(seatsIndex)

    const selectedSeatsCount = selectedSeats.length;
    console.log(selectedSeatsCount);
    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount*ticketPrice;
    reward.innerText = (selectedSeatsCount*ticketPrice)/100;

    totalReward= reward.innerText;
    totalMoney = total.innerText;
    // localStorage.setItem('priceSelectedSeats',totalMoney);
    console.log('total:',totalRoney)
    console.log('reward:',totalRoney)
    // myfunc(lol)
}

function myfunc(myvar){
    let ans = myvar.attributes.for.value;
    console.log('ans',ans)
    movieTitle = myvar.getAttribute('data-busName')
    console.log(movieTitle)
    let ans1= ans.split("#");
    var iterator = ans1.values();
    ticketPrice= iterator.next().value;
    updateSelectedCount();
}

const modalBtns = [...document.getElementsByClassName('modal-button')];
                                    // console.log(modalBtns)
const modalHeading = document.getElementById('heading');
const modalSeatMgmnt = document.getElementById('bussesSeat')
// console.log(modalHeading)



// modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
//     busId = modalBtn.getAttribute('data-busId');
//     busName = modalBtn.getAttribute('data-busName');
//     console.log ('seats',seats)
//     all_seats = modalBtn.querySelectorAll('.seat-row .seat')
//     console.log ('all_seats',all_seats)
//     const routeId = modalBtn.getAttribute('data-routeId');
//     const busSeat = modalBtn.getAttribute('data-busSeat');
//     const seatType = modalBtn.getAttribute('data-seatType');
//     busPrice= modalBtn.getAttribute('data-busPrice');
//     // console.log(busPrice)

//     localStorage.setItem('selectedBusIndex',busId);
//     localStorage.setItem('selectedBusPrice',busPrice);
//     modalHeading.innerHTML=`
//     <p class="text-center" id="heading"><b> Select ${busName} Seat</b></p>
//     `

// }))

// console.log(modalBtns.busName)



container.addEventListener('click',(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
        e.target.classList.toggle('selected')
    }
    updateSelectedCount();
})


// modal clear after closing()


// window.addEventListener('DOMContentLoaded', (event) => {
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    $(document).ready(function() {
        $('#mymodal').on('hidden.bs.modal', function() {
            history.go(0);
        });
        });
    busId = modalBtn.getAttribute('data-busId');
    busName = modalBtn.getAttribute('data-busName');
    busuniqueid =modalBtn.getAttribute('data-busuniqueid');
    // console.log ('seats',seats)
    const all_seats = document.querySelectorAll('.seat-row .seat');
    console.log ('all_seats',all_seats)
    const routeId = modalBtn.getAttribute('data-routeId');
    const busSeat = modalBtn.getAttribute('data-busSeat');
    const seatType = modalBtn.getAttribute('data-seatType');
    busPrice= modalBtn.getAttribute('data-busPrice');
    const ctaBtn = document.querySelector('button.purchase-btn')
    console.log('ctaBtn:',ctaBtn)
    // console.log('totalMoney:',totalMoney)
    // console.log(busPrice)

    localStorage.setItem('selectedBusIndex',busId);
    localStorage.setItem('selectedBusPrice',busPrice);
    localStorage.setItem('selectedBusName',busName);
    modalHeading.innerHTML=`
    <p class="text-center" id="heading"><b> Select ${busName} Seat</b></p>
    `   
    // modalSeatMgmnt.innerHTML=`
    // <div class="seat-row">

    // </div>
    // `
        // ---------------- backend stuffs---------------
    // body={busName: busName, busId: busId}
    // console.log(body)
    async function contactAPI(url,body){
        const response = await fetch(url,{
            method:"POST",
            headers:{
                "content-Type":"application/json"
            },
            body:JSON.stringify(body)
        })
        return response.json()
    }
    function getAPI(url,body){
        fetch(url,{
            method:"POST",
            headers:{
                "content-Type":"application/json"
            },
            body:JSON.stringify(body)
        })
        .then(response => {
            location.replace('http://127.0.0.1:8000/esewa_payment/?bus_id='+busId)
            console.log('then data====================')
        })
        .catch(error => {
            // handle the error
            console.log('catch data=======================')
        });
    }
    // function sendData(){
    //     fetch(url,{
    //         method:"POST",
    //         headers:{
    //             "Content-type":"application/json",
    //         }
    //         body: JSON.stringify
    //     })
    // }


    
    contactAPI("/occupied/",{busName, busId}).then(data=>{
        console.log(data)
        const occupied_seat = data["occupied_seats"]
        console.log('occupied_seat_backend',occupied_seat)
        const bus_title = data["bus"]
        const bus_iddata = data["busId"]
        console.log('bus_iddata:',bus_iddata)
        const seat_LocalStorage = localStorage.getItem('selectedSeats')?JSON.parse
        (localStorage.getItem('selectedSeats')):null
        const bus_index = localStorage.getItem('selectedBusIndex')
        const bus_name = localStorage.getItem('selectedBusName')

        const LS_bus = +bus_index
        console.log('LS_bus:',LS_bus)

        if (LS_bus == bus_iddata){
            console.log(true)
            if(occupied_seat != null && occupied_seat.length > 0){
                all_seats.forEach((seat, index)=>{
                    if(occupied_seat.indexOf(index)> -1){
                        seat.classList.add('occupied')
                        seat.classList.remove('selected')
                    }
                })
            }
            if (seat_LocalStorage != null){
                seat_LocalStorage.forEach((seat,index)=>{
                    if(occupied_seat.includes(seat)){
                        seat.localStorage.splice(index,1)
                        localStorage.setItem("selectedSeats",seat_LocalStorage)
                    }
                })
            }    
        }
        updateSelectedCount()
    })
    ctaBtn.addEventListener("click",e=>{
    // const form = document.getElementById('p-form')
    
    // const csrf = document.getElementsByName('csrfmiddlewaretoken')
    // form.addEventListener('submit',e=>{
        // const fd = new FormData()
        // fd.append('csrfmiddlewaretoken',csrf[0].value)
        // fd.append('firstName',firstName.value)
        // fd.append('lastName',lastName.value)
        // fd.append('emailId',emailId.value)
        // fd.append('phoneNumber',phoneNumber.value)
        // fd.append('pickupArea',pickuparea.value)
        // fd.append('dropArea',dropArea.value)
        const bus_title = busName
        console.log('busName:',busName)
        const bus_id = busId
        const seat_list = JSON.parse(localStorage.getItem("selectedSeats"))
        if(seat_list != null && seat_list.length > 0){
            const firstName = document.getElementById('firstnameid')
            console.log('firstName',firstName)
            const lastName = document.getElementById('lastnameid')
            const phoneNumber = document.getElementById('phonenum')
            const pickupArea = document.getElementById('pickuparea')
            const dropArea = document.getElementById('droparea')
            data={
                bus_title,
                bus_id,
                seat_list,
                'firstName':firstName.value,
                'lastName':lastName.value,
                'phoneNumber':phoneNumber.value,
                'pickupArea':pickupArea.value,
                'dropArea':dropArea.value


            }
            console.log('api before data',data)
            getAPI("/payment/",data)
            // $.ajax({
            //     url:"/payment/",
            //     type:"POST",
            //     data:busdata,
            //     dataType:"json",
            //     success : function(data){
            //         console.log('ajax-data:',data)
            //     },

            // });
            // .then(res=>{
            //     if(res["payment_url"]){
            //         //redirect the customer
            //         window.location.href = res["payment_url"]
            //     }else{
            //         console.log('error')
            //     }
            // }).catch(e=>{
            //     console.log(e)
            // })
        }
    })


function printData()
{
   var divToPrint=document.getElementById("printTable");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();
   newWin.close();
}

$('#printme').on('click',function(){
printData();
})
    // const form = document.getElementById('p-form')
    // const firstName = document.getElementById('firstnameid')
    // const lastName = document.getElementById('lastnameid')
    // const emailId = document.getElementById('emailid')
    // const phoneNumber = document.getElementById('phonenum')
    // const pickupArea = document.getElementById('pickuparea')
    // const dropArea = document.getElementById('droparea')
    // const csrf = document.getElementsByName('csrfmiddlewaretoken')
    // form.addEventListener('submit',e=>{
    //     const fd = new FormData()
    //     fd.append('csrfmiddlewaretoken',csrf[0].value)
    //     fd.append('firstName',firstName.value)
    //     fd.append('lastName',lastName.value)
    //     fd.append('emailId',emailId.value)
    //     fd.append('phoneNumber',phoneNumber.value)
    //     fd.append('pickupArea',pickuparea.value)
    //     fd.append('dropArea',dropArea.value)
    //     $.ajax({
    //         type: 'POST',
    //         url: url,
    //         enctype: 'multipart/form-data',
    //         data:fd,
    //         success: function(response){
    //             console.log(response)
    //         },
    //         error:function(error){
    //             console.log(error)
    //         },
    //         cache:false,
    //         contentType:false,
    //         processData:false
    //     })
    // })

    // console.log(form)
    // paypal
    // const totalMoney = localStorage.getItem('priceSelectedSeats')
    // console.log('totalMoney:',totalMoney)
    // forEach(updateSelectedCount(){
    //     amount
    // }
    //     )
    // document.addEventListener("DOMContentLoaded", function(){
    //     //dom is fully loaded, but maybe waiting on images & css files
    // });
    // paypal.Buttons({
    //     style: {
    //         color:  'blue',
    //         shape:  'pill',
    //         label:  'pay',
    //         height: 40
    //     },

    //     // Set up the transaction
    //     createOrder: function(data, actions) {
    //         return actions.order.create({
    //             purchase_units: [{
    //                 amount: {
    //                     value: '5.44'
    //                 }
    //             }]
    //         });
    //     },

    //     // Finalize the transaction
    //     onApprove: function(data, actions) {
    //         return actions.order.capture().then(function(orderData) {
    //             // Successful capture! For demo purposes:
    //             console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
    //             var transaction = orderData.purchase_units[0].payments.captures[0];
    //             alert('Transaction '+ transaction.status + ': ' + transaction.id + '\n\nSee console for all available details');

    //             // Replace the above to show a success message within this page, e.g.
    //             // const element = document.getElementById('paypal-button-container');
    //             // element.innerHTML = '';
    //             // element.innerHTML = '<h3>Thank you for your payment!</h3>';
    //             // Or go to another URL:  actions.redirect('thank_you.html');
    //         });
    //     }


    // }).render('#paypal-button-container');

}))
// });
