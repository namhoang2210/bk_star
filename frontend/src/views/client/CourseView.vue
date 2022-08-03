<template>
  <Header msg="Welcome to Website"/>

  <div class="mt-36">
       <div class="px-4 md:px-[17%] mt-16 text-gray-800">
        <div class="grid md:grid-cols-2 xl:grid-cols-4 md:gap-6">
            <div class="text-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 mx-auto text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                <div class="text-lg font-semibold mt-3 md:h-14">Đội ngũ giáo viên giàu kinh nghiệm</div>
                <p class="mt-2 text-gray-600">100% giáo viên tốt nghiệp đại học Top 10-20 của Mỹ</p>
            </div>
            <div class="text-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 mx-auto text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                <div class="text-lg font-semibold mt-3 md:h-14">Phương pháp giảng dạy độc quyền từ Mỹ</div>
                <p class="mt-2 text-gray-600">Giáo trình được biên soạn bởi các chuyên gia Mỹ giàu kinh nghiêm tốt nghiệp các trường ĐH hàng đầu Mỹ</p>
            </div>
             <div class="text-center mb-4">
               <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 mx-auto text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
                <div class="text-lg font-semibold mt-3 md:h-14">Kiểm tra trình độ miễn phí</div>
                <p class="mt-2 text-gray-600">Phân tích điểm mạnh điểm yếu của học viên trên máy</p>
            </div>
            <div class="text-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 mx-auto text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
                </svg>
                <div class="text-lg font-semibold mt-3 md:h-14">Cam kết chất lượng đầu ra</div>
                <p class="mt-2 text-gray-600">100% Học sinh của chúng tôi tăng điểm sau mỗi khóa học</p>
            </div>
        </div>
        <div class="grid grid-cols-3  xl:grid-cols-6 gap-6 mt-12">
            <div class="mb-4 ">
                <img class="rounded-lg " src="https://americanstudy.edu.vn/wp-content/uploads/2020/05/IELTS-150x150-1-150x150.jpg" alt="">
            </div>
            <div class="mb-4">
                <img class="rounded-lg" src="https://americanstudy.edu.vn/wp-content/uploads/2020/05/TOEFL.jpg" alt="">
            </div>
            <div class="mb-4">
                <img class="rounded-lg" src="https://americanstudy.edu.vn/wp-content/uploads/2020/05/SSAT-150x150-1-150x150.jpg" alt="">
            </div>
            <div class="mb-4">
                <img class="rounded-lg" src="https://americanstudy.edu.vn/wp-content/uploads/2020/05/SAT-150x150-1-150x150.jpg" alt="">
            </div>
            <div class="mb-4">
                <img class="rounded-lg" src="https://americanstudy.edu.vn/wp-content/uploads/2020/05/ACT-150x150-1-150x150.png" alt="">
            </div>
            <div class="mb-4">
                <img class="rounded-lg" src="https://americanstudy.edu.vn/wp-content/uploads/2020/05/AP-150x150-1-150x150.jpg" alt="">
            </div>
        </div>
        <div>
            <div class="text-4xl font-semibold text-gray-800 text-center pt-14 uppercase">Danh sách giảng viên</div>
            <hr class="h-2 w-[50px] mx-auto bg-[#011858] mt-8 rounded-full">
            <div class="grid md:grid-cols-2 xl:grid-cols-4 md:gap-6 mt-6">
                <div class="text-center mb-6">
                    <img class="w-32 h-32 rounded-full mx-auto" src="https://images.unsplash.com/photo-1493752603190-08d8b5d1781d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8cGVvcGxlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="" />
                    <h1 class="text-lg font-semibold mt-2">Adam Wathan</h1>
                    <hr class="w-8 mx-auto my-2 h-1 bg-gray-500">
                    <p>Giảng viên Tiếng Anh với 10 năm kinh nghiệm</p>
                </div>
                <div class="text-center mb-6">
                    <img class="w-32 h-32 rounded-full mx-auto" src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fHBlb3BsZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60" alt="" />
                    <h1 class="text-lg font-semibold mt-2">Adam Wathan</h1>
                    <hr class="w-8 mx-auto my-2 h-1 bg-gray-500">
                    <p>Giảng viên Tiếng Anh với 10 năm kinh nghiệm</p>
                </div>
                <div class="text-center mb-6">
                    <img class="w-32 h-32 rounded-full mx-auto" src="https://images.unsplash.com/photo-1499887142886-791eca5918cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fHBlb3BsZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60" alt="" />
                    <h1 class="text-lg font-semibold mt-2">Adam Wathan</h1>
                    <hr class="w-8 mx-auto my-2 h-1 bg-gray-500">
                    <p>Giảng viên Tiếng Anh với 10 năm kinh nghiệm</p>
                </div>
                <div class="text-center mb-6">
                    <img class="w-32 h-32 rounded-full mx-auto" src="https://images.unsplash.com/photo-1479936343636-73cdc5aae0c3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHBlb3BsZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60" alt="" />
                    <h1 class="text-lg font-semibold mt-2">Adam Wathan</h1>
                    <hr class="w-8 mx-auto my-2 h-1 bg-gray-500">
                    <p>Giảng viên Tiếng Anh với 10 năm kinh nghiệm</p>
                </div>
            </div>
        </div>
        <div>
            <div class="text-4xl font-semibold text-gray-800 text-center pt-14 uppercase">Học viên nổi bật</div>
            <hr class="h-2 w-[50px] mx-auto bg-[#011858] mt-8 rounded-full">
            <div class="grid lg:grid-cols-3 md:gap-6 mt-6">
                <div class="text-sm leading-6 mb-4">
                    <div class="relative flex flex-col-reverse bg-slate-50 rounded-lg p-6 ">
                        <div class="mt-6 text-slate-700 ">
                            <p>Cảm nhận của học viên, Have been working with CSS for over ten years and Tailwind just makes my life easier. It is still CSS and you use flex, grid, etc. but just quicker to write and maintain.</p>
                        </div>
                        <div class="flex items-center space-x-4">
                            <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YXZhdGFyfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="" class="flex-none w-14 h-14 rounded-full object-cover" loading="lazy">
                            <div class="flex-auto"><div class="text-base text-slate-900 font-semibold ">
                                <a href="" tabindex="0">
                                    <span class="absolute inset-0"></span>Lê Hoàng Nam
                                </a>
                            </div>
                        <div class="mt-0.5">Học bổng 4.6 tỉ HVCNBCVT</div>
                    </div>
                    </div></div>
                </div>
                <div class="text-sm leading-6 mb-4">
                    <div class="relative flex flex-col-reverse bg-slate-50 rounded-lg p-6 ">
                        <div class="mt-6 text-slate-700 ">
                            <p>Cảm nhận của học viên, Have been working with CSS for over ten years and Tailwind just makes my life easier. It is still CSS and you use flex, grid, etc. but just quicker to write and maintain.</p>
                        </div>
                        <div class="flex items-center space-x-4">
                            <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YXZhdGFyfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="" class="flex-none w-14 h-14 rounded-full object-cover" loading="lazy">
                            <div class="flex-auto"><div class="text-base text-slate-900 font-semibold ">
                                <a href="" tabindex="0">
                                    <span class="absolute inset-0"></span>Lê Hoàng Nam
                                </a>
                            </div>
                        <div class="mt-0.5">Học bổng 4.6 tỉ HVCNBCVT</div>
                    </div>
                    </div></div>
                </div>
                <div class="text-sm leading-6 mb-4">
                    <div class="relative flex flex-col-reverse bg-slate-50 rounded-lg p-6 ">
                        <div class="mt-6 text-slate-700 ">
                            <p>Cảm nhận của học viên, Have been working with CSS for over ten years and Tailwind just makes my life easier. It is still CSS and you use flex, grid, etc. but just quicker to write and maintain.</p>
                        </div>
                        <div class="flex items-center space-x-4">
                            <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YXZhdGFyfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="" class="flex-none w-14 h-14 rounded-full object-cover" loading="lazy">
                            <div class="flex-auto"><div class="text-base text-slate-900 font-semibold ">
                                <a href="" tabindex="0">
                                    <span class="absolute inset-0"></span>Lê Hoàng Nam
                                </a>
                            </div>
                        <div class="mt-0.5">Học bổng 4.6 tỉ HVCNBCVT</div>
                    </div>
                    </div></div>
                </div>
            </div>

        </div>
        <div class="w-full">
			<div class="flex justify-center  my-12">
				<!-- Row -->
				<div class="w-full flex">
					<!-- Col -->
					<div class="w-full h-auto bg-gray-400 hidden lg:block lg:w-5/12 bg-cover rounded-l-lg">
                        <img class="h-full rounded-l-lg" src="https://images.unsplash.com/photo-1587613863965-74d82b39ef79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTl8fHN0dWR5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60" alt="">
                    </div>
					<!-- Col -->
					<div class="w-full lg:w-7/12 bg-white p-5 rounded-lg lg:rounded-l-none">
						<h3 class="pt-4 text-2xl text-center">💖 Đăng kí ngay 💖💖</h3>
						<form class="px-8 pt-6 pb-8 mb-4 bg-white rounded">
							<div class="mb-4">
								<label class="block mb-2 text-sm font-bold text-gray-700" for="email">
									Họ tên
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded  appearance-none focus:outline-none focus:shadow-outline"
									id="name"
									type="text"
									placeholder="Họ và tên"
								/>
							</div>
							<div class="mb-4">
								<label class="block mb-2 text-sm font-bold text-gray-700" for="email">
									Email
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded  appearance-none focus:outline-none focus:shadow-outline"
									id="email"
									type="email"
									placeholder="Email"
								/>
							</div>
							<div class="mb-4">
								<label class="block mb-2 text-sm font-bold text-gray-700" for="email">
									Số điện thoại
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded  appearance-none focus:outline-none focus:shadow-outline"
									id="phone"
									type="number"
									placeholder="Số điện thoại"
								/>
							</div>
                            <div class=" grid grid-cols-2 gap-4 md:gap-8">
                                <div class="flex items-center mb-4">
                                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 ">
                                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900">Khóa học IELTS</label>
                                </div>
                                <div class="flex items-center mb-4">
                                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 ">
                                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900">Khóa học IELTS</label>
                                </div>
                                <div class="flex items-center mb-4">
                                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 ">
                                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900">Khóa học IELTS</label>
                                </div>
                                <div class="flex items-center mb-4">
                                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 ">
                                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900">Khóa học IELTS</label>
                                </div>
                                <div class="flex items-center mb-4">
                                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 ">
                                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900">Khóa học IELTS</label>
                                </div>
                                <div class="flex items-center mb-4">
                                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 ">
                                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900">Khóa học IELTS</label>
                                </div>
                            </div>

							<div class="mt-6 text-center">
								<button
									class="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 focus:outline-none focus:shadow-outline"
									type="button"
								>
									Đăng kí
								</button>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
   </div>
  </div>

  <Footer msg="This is Footer"/>
</template>

<script>
// @ is an alias to /src
import { Header, Footer } from '@/components'

export default {
  components: {
    Header,
    Footer
  }
}
</script>
