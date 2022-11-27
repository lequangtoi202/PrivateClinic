(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


    // Date and time picker
    $('.date').datetimepicker({
        format: 'L'
    });
    $('.time').datetimepicker({
        format: 'LT'
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 300, 'easeInOutExpo');
        return false;
    });


    // Price carousel
    $(".price-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 45,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });


    // Team carousel
    $(".team-carousel, .related-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 45,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
    });



})(jQuery);

function find_patient_by_id(param) {
    fetch('/api/find_patient_by_id/' + param.value, {
      method: "GET",
      dataType: 'json',
      ContentType: 'application/json'
    }).then(res => res.json()).then(data => {
        hoTen = document.getElementById("hoTen");
        hoTen.value  = data.hoTen
    }).catch((err) => {
      console.log(err)
    })
}

``


//function addCode() {
//    fetch('/api/get_all_medicines', {
//        method: "GET",
//        dataType: 'json',
//        ContentType: 'application/json'
//    }).then(res => res.json()).then(data => {
//        add = document.getElementById("add-row");
//
//        add.innerHTML += `<tr>
//                                <td style="width: 300px;">
//                                    <div class=" time bg-light border-0">
//                                        <select name="tenThuoc" class="thuoc"
//                                                style="width: 100%;height: 40px;border: none;outline: none; border-radius: 8px;">
//                                            <option value="">Không</option>
//                                        </select>
//                                    </div>
//                                </td>
//                                <td>
//                                    <input type="number" class="form-control" required name="soLuong" min="0" max="100">
//                                </td>
//                                <td>
//                                    <textarea class="form-control" required name="cachDung"></textarea>
//                                </td>
//                            </tr>`
//        data.forEach(m => {
//            sl = document.getElementsByTagName('select')
//            console.log(sl);
//            var opt = document.createElement('option');
//            opt.value = m.maThuoc;
//            opt.innerHTML = m.tenThuoc;
//            sl.add(opt);
//        })
//    }).catch((err) => {
//      console.log(err)
//    })
//}
listD = []
function add(){
    soLuong = document.getElementById('soLuong')
    cachDung = document.getElementById('cachDung')
    table = document.getElementById('table')
    thuoc = document.getElementById('thuoc')
    if (thuoc.value != '' && soLuong.value != '' && cachDung.value != '')
    {
        listD.push({
        "tenThuoc": thuoc.options[thuoc.selectedIndex].text,
        "thuoc": thuoc.value,
        "soLuong": soLuong.value,
        "cachDung": cachDung.value
        })
    }
    soLuong.value=''
    cachDung.value=''
    table.innerHTML = ''
    for (let i = 0; i< listD.length; i++){
        table.innerHTML += `<tr>
                            <td style="width: 500px;">
                                <input name="thuoc" hidden value="${listD[i].thuoc}" />
                                <div style="width:100%;">${listD[i].tenThuoc}<div/>
                            </td>
                            <td>
                                <input class="border-0" style="outline: none; width:100%;" name="soLuong" value="${listD[i].soLuong}"/>
                            </td>
                            <td>
                                <input class="border-0" style="outline: none; width:100%;"" name="cachDung" value="${listD[i].cachDung}"/>
                            </td>
                            <td>
                                <div class="m-auto"><input type="button" class="btn btn-danger" onclick="deleteRow(this)"
                                                           value="Xóa"/></div>
                            </td>
                        </tr>`
    }
}

function deleteRow(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true)
    document.getElementById("table").deleteRow(i-1);
}


function payment(){
    tien_kham = document.getElementById('tien_kham').innerText.trim().split(" ")[0]
    tien_thuoc = document.getElementById('tien_thuoc').innerText.trim().split(" ")[0]
    tong_tien = document.getElementById('tong_tien').innerText.trim().split(" ")[0]
    maPK = document.getElementById('maPK').value
    if (tien_thuoc != '' || tien_thuoc != 0.0 && tien_kham != '' || tien_kham != 0.0 && tong_tien != '' || tong_tien != 0.0)
    {
        fetch('/api/employee/payment', {
            method: "post",
            body: JSON.stringify({
                "tien_kham": parseFloat(tien_kham.replace(',', '')),
                "tien_thuoc": parseFloat(tien_thuoc.replace(',', '')),
                "tong_tien": parseFloat(tong_tien.replace(',', '')),
                "maPK": parseInt(maPK)
            }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(res => res.json()).then((data) => {
            if (data.status === 200)
            {
                window.location.href= 'http://127.0.0.1:5000/employee/payment';
                alert('Thanh toán thành công')
            }



        }) // promise
    }

}