<template>
    <div id="carouselExampleIndicators" class="carousel slide relative" data-bs-ride="carousel">
    <div class="carousel-indicators absolute right-0 bottom-0 left-0 flex justify-center p-0 mb-4">
      <button type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="0"
        class="active"
        aria-current="true"
        aria-label="Slide 1"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="1"
        aria-label="Slide 2"
      ></button>
    </div>
    <div class="carousel-inner relative w-full overflow-hidden">
      <div class="carousel-item active float-left w-full">
        <img
          src="https://scontent.fhan5-3.fna.fbcdn.net/v/t39.30808-6/240491630_390643405907881_5641940386351270480_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e3f864&_nc_eui2=AeHqtVFiz6zcohNHqNGHZ5YdK2kRL70JkK8raREvvQmQrwaHKtonr1cYNMmy-AAAcOqjLJUJP5vumAbxXMfSLmdC&_nc_ohc=Gn9VR-5AR0MAX_h1_PQ&_nc_ht=scontent.fhan5-3.fna&oh=00_AT_Rtjfa39C5WhQn1BC_FdalGyWDjuJFUfn_CxVrJzmxZQ&oe=62D033A0"
          class="block w-full  h-[250px] md:h-[400px] lg:h-[600px] object-cover"
          alt="Banner 1"
        />
      </div>
      <div class="carousel-item float-left w-full">
        <img
          src="https://scontent.fhan5-8.fna.fbcdn.net/v/t1.6435-9/103558363_152978349674389_1997969188172033568_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=e3f864&_nc_eui2=AeFf5TK-ZuIR7Ov6jpJxXq9UE9JHPF0607kT0kc8XTrTuc82OAII4z8bjrgH11yXKZtTxbbCG_-CA6HYhTTVds-1&_nc_ohc=xeT_-Ry6bHwAX-i1ue_&tn=DEq0oQOlsqXiz2Kk&_nc_ht=scontent.fhan5-8.fna&oh=00_AT_B3BSBkDp6DMtTbjp4h9YCseXI6ylAL--u_t7sSMtE0Q&oe=62F10BB8"
          class="block w-full  h-[250px] md:h-[400px] lg:h-[600px] object-cover"
          alt="Banner 2"
        />
      </div>
    </div>
    <button
      class="carousel-control-prev absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline left-0"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon inline-block bg-no-repeat" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline right-0"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon inline-block bg-no-repeat" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
</div>
<!-- <div class="bg-[#011858] text-white grid lg:grid-cols-5 py-10 gap-10 font-bold grid-cols-3 px-3 lg:px-[15%]">
    <div class="text-center">
        <div class="lg:text-5xl text-2xl font-bold">85+</div>
        <div class="lg:text-lg text-sm pt-2">
            Tựa game mobie <br>
            đã phát hành
        </div>
    </div>
    <div class="text-center">
        <div class="lg:text-5xl text-2xl font-bold whitespace-nowrap">42 Triệu</div>
        <div class="lg:text-lg text-sm pt-2">
            Khách hàng <br>
            toàn cầu
        </div>
    </div>
    <div class="text-center">
        <div class="lg:text-5xl text-2xl font-bold">10</div>
        <div class="lg:text-lg text-sm pt-2">
           Thị trường <br>
           nước ngoài
        </div>
    </div>
    <div class="text-center">
        <div class="lg:text-5xl text-2xl font-bold">600+</div>
        <div class="lg:text-lg text-sm pt-2">
            Nhân sự tại <br>
            Hà Nội và Tp.HCM
        </div>
    </div>
    <div class="text-center">
        <div class="lg:text-5xl text-2xl font-bold">2</div>
        <div class="lg:text-lg text-sm pt-2">
            Văn phòng tại <br>
            Hà Nội và Tp.HCM
        </div>
    </div>
</div> -->
</template>

<script>
export default {
  name: 'Banner',
  props: {
    msg: String
  },
}
</script>