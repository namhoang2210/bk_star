<template>
  <div>
    <Header msg="Welcome to Website"/>
    <Banner msg="This is banner"/>
    <div class="lg:flex justify-between px-4 md:px-[15%] mt-10 md:mt-16">
      <div class="font-bold lg:text-5xl text-center lg:text-start text-2xl pb-6">Chỗ này là slogan</div>
      <div class="lg:w-1/2">
        <p>Giới thiệu blabla...Thành lập tháng 5/2015 với sứ mệnh mang đến trải nghiệm giải trí và giá trị tri thức cho
          cộng đồng thông qua các sản phẩm công nghệ, Funtap đã phát triển nhanh chóng và trở thành một trong những nhà
          phát hành game trên di động hàng đầu Việt Nam .</p>
        <router-link to="/about" class="flex justify-center lg:justify-start">
          <button class="px-6 py-2 rounded bg-[#011858] text-white hover:bg-blue-700 mt-6 lg:mt-4">Về chúng tôi</button>
        </router-link>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-2 xl:grid-cols-4 mt-12 bg-white  mx-4 md:mx-[15%]">
    <sub-category v-for="category in subCategories" :key="category.id" :category="category"/>
  </div>
  <section
      class="container mt-14 flex items-center justify-center h-[300px] md:h-[400px] lg:h-[520px] m-auto w-full bg-fixed bg-center bg-cover custom-img"
  >
    <div class="p-5 text-2xl text-white bg-purple-300 bg-opacity-50 rounded-xl">
      Cái Parralax CSS này hay nhưng chưa biết nhét content j vào đây
    </div>
  </section>
  <div class=" bg-white px-[15%] ">
    <div class="text-4xl font-semibold text-gray-800 text-center pt-14 uppercase">Tin tức - Sự kiện</div>
    <hr class="h-2 w-[50px] mx-auto bg-[#011858] mt-8 rounded-full">
    <div class="py-10 grid lg:grid-cols-3 gap-6">
      <div class="">
        <div class="border-2 border-gray-200 rounded-lg mb-4">
          <img class="object-cover object-center w-full lg:h-48 md:h-36 rounded-t-lg"
               src="https://source.unsplash.com/random" alt="blog">
          <div class="p-6">
            <h1 class="mb-2 text-lg font-medium  h-[60px] text-ellipsis overflow-hidden text-gray-900">
              <a class="hover:text-blue-600" href="">📢📢📢 THÔNG BÁO TUYỂN THÀNH VIÊN BK STAR TEAM❗❗❗</a>
            </h1>
            <div class="flex gap-1 items-center text-sm text-gray-500 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                30 Tháng 9, 2021
              </div>

            </div>
            <p class="mb-2 text-sm tracking-wide text-gray-700 h-[100px] text-ellipsis overflow-hidden">
              Để nâng cao chất lượng hoạt động, tăng cường nhân lực và phát hiện các tài năng
              mới cho các hoạt động và sinh hoạt của CLB BK STAR trong thời gian tới, CLB BK STAR tổ
              chức tuyển thành viên.
            </p>
            <div class="flex items-center ">
              <a href=""
                 class="inline-flex items-center hover:text-blue-800 text-indigo-500 cursor-pointer md:mb-2 lg:mb-0">Đọc
                tiếp
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 mt-1" fill="none"
                     viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </a>

            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="border-2 border-gray-200 rounded-lg mb-4">
          <img class="object-cover object-center w-full lg:h-48 md:h-36 rounded-t-lg"
               src="https://source.unsplash.com/random" alt="blog">
          <div class="p-6">
            <h1 class="mb-2 text-lg font-medium  h-[60px] text-ellipsis overflow-hidden text-gray-900">
              <a class="hover:text-blue-600" href="">📢📢📢 THÔNG BÁO TUYỂN THÀNH VIÊN BK STAR TEAM❗❗❗</a>
            </h1>
            <div class="flex gap-1 items-center text-sm text-gray-500 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                30 Tháng 9, 2021
              </div>

            </div>
            <p class="mb-2 text-sm tracking-wide text-gray-700 h-[100px] text-ellipsis overflow-hidden">
              Để nâng cao chất lượng hoạt động, tăng cường nhân lực và phát hiện các tài năng
              mới cho các hoạt động và sinh hoạt của CLB BK STAR trong thời gian tới, CLB BK STAR tổ
              chức tuyển thành viên.
            </p>
            <div class="flex items-center ">
              <a href=""
                 class="inline-flex items-center hover:text-blue-800 text-indigo-500 cursor-pointer md:mb-2 lg:mb-0">Đọc
                tiếp
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 mt-1" fill="none"
                     viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </a>

            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="border-2 border-gray-200 rounded-lg mb-4">
          <img class="object-cover object-center w-full lg:h-48 md:h-36 rounded-t-lg"
               src="https://source.unsplash.com/random" alt="blog">
          <div class="p-6">
            <h1 class="mb-2 text-lg font-medium  h-[60px] text-ellipsis overflow-hidden text-gray-900">
              <a class="hover:text-blue-600" href="">📢📢📢 THÔNG BÁO TUYỂN THÀNH VIÊN BK STAR TEAM❗❗❗</a>
            </h1>
            <div class="flex gap-1 items-center text-sm text-gray-500 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                30 Tháng 9, 2021
              </div>

            </div>
            <p class="mb-2 text-sm tracking-wide text-gray-700 h-[100px] text-ellipsis overflow-hidden">
              Để nâng cao chất lượng hoạt động, tăng cường nhân lực và phát hiện các tài năng
              mới cho các hoạt động và sinh hoạt của CLB BK STAR trong thời gian tới, CLB BK STAR tổ
              chức tuyển thành viên.
            </p>
            <div class="flex items-center ">
              <a href=""
                 class="inline-flex items-center hover:text-blue-800 text-indigo-500 cursor-pointer md:mb-2 lg:mb-0">Đọc
                tiếp
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 mt-1" fill="none"
                     viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="border-2 border-gray-200 rounded-lg mb-4">
          <img class="object-cover object-center w-full lg:h-48 md:h-36 rounded-t-lg"
               src="https://source.unsplash.com/random" alt="blog">
          <div class="p-6">
            <h1 class="mb-2 text-lg font-medium  h-[60px] text-ellipsis overflow-hidden text-gray-900">
              <a class="hover:text-blue-600" href="">📢📢📢 THÔNG BÁO TUYỂN THÀNH VIÊN BK STAR TEAM❗❗❗</a>
            </h1>
            <div class="flex gap-1 items-center text-sm text-gray-500 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                30 Tháng 9, 2021
              </div>

            </div>
            <p class="mb-2 text-sm tracking-wide text-gray-700 h-[100px] text-ellipsis overflow-hidden">
              Để nâng cao chất lượng hoạt động, tăng cường nhân lực và phát hiện các tài năng
              mới cho các hoạt động và sinh hoạt của CLB BK STAR trong thời gian tới, CLB BK STAR tổ
              chức tuyển thành viên.
            </p>
            <div class="flex items-center ">
              <a href=""
                 class="inline-flex items-center hover:text-blue-800 text-indigo-500 cursor-pointer md:mb-2 lg:mb-0">Đọc
                tiếp
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 mt-1" fill="none"
                     viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </a>

            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="border-2 border-gray-200 rounded-lg mb-4">
          <img class="object-cover object-center w-full lg:h-48 md:h-36 rounded-t-lg"
               src="https://source.unsplash.com/random" alt="blog">
          <div class="p-6">
            <h1 class="mb-2 text-lg font-medium  h-[60px] text-ellipsis overflow-hidden text-gray-900">
              <a class="hover:text-blue-600" href="">📢📢📢 THÔNG BÁO TUYỂN THÀNH VIÊN BK STAR TEAM❗❗❗</a>
            </h1>
            <div class="flex gap-1 items-center text-sm text-gray-500 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                30 Tháng 9, 2021
              </div>

            </div>
            <p class="mb-2 text-sm tracking-wide text-gray-700 h-[100px] text-ellipsis overflow-hidden">
              Để nâng cao chất lượng hoạt động, tăng cường nhân lực và phát hiện các tài năng
              mới cho các hoạt động và sinh hoạt của CLB BK STAR trong thời gian tới, CLB BK STAR tổ
              chức tuyển thành viên.
            </p>
            <div class="flex items-center ">
              <a href=""
                 class="inline-flex items-center hover:text-blue-800 text-indigo-500 cursor-pointer md:mb-2 lg:mb-0">Đọc
                tiếp
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 mt-1" fill="none"
                     viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </a>

            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="border-2 border-gray-200 rounded-lg mb-4">
          <img class="object-cover object-center w-full lg:h-48 md:h-36 rounded-t-lg"
               src="https://source.unsplash.com/random" alt="blog">
          <div class="p-6">
            <h1 class="mb-2 text-lg font-medium  h-[60px] text-ellipsis overflow-hidden text-gray-900">
              <a class="hover:text-blue-600" href="">📢📢📢 THÔNG BÁO TUYỂN THÀNH VIÊN BK STAR TEAM❗❗❗</a>
            </h1>
            <div class="flex gap-1 items-center text-sm text-gray-500 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                30 Tháng 9, 2021
              </div>

            </div>
            <p class="mb-2 text-sm tracking-wide text-gray-700 h-[100px] text-ellipsis overflow-hidden">
              Để nâng cao chất lượng hoạt động, tăng cường nhân lực và phát hiện các tài năng
              mới cho các hoạt động và sinh hoạt của CLB BK STAR trong thời gian tới, CLB BK STAR tổ
              chức tuyển thành viên.
            </p>
            <div class="flex items-center ">
              <a href=""
                 class="inline-flex items-center hover:text-blue-800 text-indigo-500 cursor-pointer md:mb-2 lg:mb-0">Đọc
                tiếp
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 mt-1" fill="none"
                     viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                </svg>
              </a>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <Footer msg="This is footer"/>
</template>

<script>
// @ is an alias to /src
import {defineComponent} from "vue";
import {Header, Banner, Footer, SubCategory} from '@/components'

export default defineComponent({
  name: 'HomeView',
  components: {
    Header,
    Banner,
    Footer,
    SubCategory
  },
  setup() {
    const subCategories = [
      {
        id: 1,
        name: 'Giáo dục STEAM',
        img: 'https://images.unsplash.com/photo-1638153534717-fb17b6d19040?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=435&q=80',
        title: 'Kinh nghiệm phát hành game mobile với 5 ngôn ngữ chính: Tiếng Anh, Tiếng Việt, Tiếng Thái, Tiếng Trung Quốc và Tiếng Indonesia.'
      },
      {
        id: 2,
        name: 'Tư vấn du học',
        img: 'https://images.unsplash.com/photo-1652376933844-2b4b44523549?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDR8YWV1NnJMLWo2ZXd8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60',
        title: 'Tự hào mang lại dịch vụ giải trí với chất lượng tuyệt hảo cho hơn 42 triệu khách hàng toàn cầu.'
      },
      {
        id: 3,
        name: 'Ôn Thi',
        img: 'https://images.unsplash.com/photo-1657672733176-b48c9b0eec0f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDI0fGFldTZyTC1qNmV3fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
        title: 'Kinh nghiệm phát hành game mobile với 5 ngôn ngữ chính: Tiếng Anh, Tiếng Việt, Tiếng Thái, Tiếng Trung Quốc và Tiếng Indonesia.'
      },
      {
        id: 4,
        name: 'Toán Cao Cấp',
        img: 'https://images.unsplash.com/photo-1657672733176-b48c9b0eec0f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDI0fGFldTZyTC1qNmV3fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
        title: 'Kinh nghiệm phát hành game mobile với 5 ngôn ngữ chính: Tiếng Anh, Tiếng Việt, Tiếng Thái, Tiếng Trung Quốc và Tiếng Indonesia.'
      }
    ]
    return {
      subCategories
    }
  }
})
</script>
<style>
.custom-img {
  background-image: url("https://images.unsplash.com/photo-1657524433787-a30cefc92661?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80");
}
</style>
