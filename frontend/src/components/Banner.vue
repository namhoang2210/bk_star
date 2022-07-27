<template>
    <div id="carouselExampleIndicators" class="carousel slide relative mt-20" data-bs-ride="carousel">
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
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="2"
        aria-label="Slide 3"
      ></button>
    </div>
    <div class="carousel-inner relative w-full overflow-hidden">
      <div class="carousel-item active float-left w-full">
        <img
          src="https://images.unsplash.com/photo-1657819307873-c57e45f65f6d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1332&q=80"
          class="block w-full  h-[250px] md:h-[400px] lg:h-[500px] object-cover"
          alt="Banner 1"
        />
      </div>
      <div class="carousel-item float-left w-full">
        <img
          src="https://images.unsplash.com/photo-1657659558323-08b7854ed766?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"
          class="block w-full  h-[250px] md:h-[400px] lg:h-[500px] object-cover"
          alt="Banner 2"
        />
      </div>
      <div class="carousel-item float-left w-full">
        <img
          src="https://images.unsplash.com/photo-1618171889969-0feeb769fe78?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          class="block w-full  h-[250px] md:h-[400px] lg:h-[500px] object-cover"
          alt="Banner 3"
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