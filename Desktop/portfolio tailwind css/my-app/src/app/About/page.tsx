
      import React from 'react';

export default function AboutMe() {
  return (
    
   <div className="bg-gradient-to-r from-pink-400 to-blue-800 text-white">


          <div className="text-center md:text-left md:ml-8 space-y-4 px-6">
            <h1 className="text-4xl md:text-5xl font-extrabold leading-tight mb-4 text-yellow-400">
              Hi, I m <span className="text-yellow-400">Saba Riaz</span>
            </h1>
            <p className="text-lg md:text-2xl opacity-90">
              I am a passionate UI/UX Designer focused on creating beautiful and user-friendly experiences. 
              I believe in a user-centered design approach, solving real-world problems creatively and efficiently.
            </p>
        

      
      <section className="py-16 bg-gray-900 text-white">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-8">Skills</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-8">
            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">UI Design</h3>
              <div className="flex justify-center items-center">
                <i className="fas fa-paint-brush text-3xl text-yellow-400"></i>
              </div>
            </div>

            {/* Skill Card */}
            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">UX Research</h3>
              <div className="flex justify-center items-center">
                <i className="fas fa-search text-3xl text-yellow-400"></i>
              </div>
            </div>

            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Prototyping</h3>
              <div className="flex justify-center items-center">
                <i className="fas fa-cogs text-3xl text-yellow-400"></i>
              </div>
            </div>

            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Web Design</h3>
              <div className="flex justify-center items-center">
                <i className="fas fa-laptop-code text-3xl text-yellow-400"></i>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white text-gray-800">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-8">Experience</h2>
          <div className="space-y-8">
            <div className="flex justify-center items-center space-x-4">
              <div className="w-12 h-12 bg-yellow-400 rounded-full flex justify-center items-center text-white">
                <i className="fas fa-briefcase text-xl"></i>
              </div>
              <div>
                <h3 className="text-2xl font-semibold">UI/UX Designer at XYZ Company</h3>
                <p className="text-lg opacity-80">June 2020 - Present</p>
                <p className="mt-4">Led a team of designers to create seamless digital experiences for web and mobile platforms.</p>
              </div>
            </div>

            <div className="flex justify-center items-center space-x-4">
              <div className="w-12 h-12 bg-yellow-400 rounded-full flex justify-center items-center text-white">
                <i className="fas fa-briefcase text-xl"></i>
              </div>
              <div>
                <h3 className="text-2xl font-semibold">Freelance UI/UX Designer</h3>
                <p className="text-lg opacity-80">2018 - 2020</p>
                <p className="mt-4">Worked with multiple clients to deliver high-quality UI/UX design solutions.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="py-16 bg-gray-900 text-white">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-8">Projects</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Project One</h3>
              <p className="text-lg mb-4">A web design project for an e-commerce platform. The focus was on user-friendly navigation and an intuitive shopping experience.</p>
              <a href="#" className="text-yellow-400 hover:text-yellow-500">View Project</a>
            </div>
</div>
</div>

            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Project Two</h3>
              <p className="text-lg mb-4">A mobile app design for a fitness tracking application. It included tracking user progress and integrating social features.</p>
              <a href="#" className="text-yellow-400 hover:text-yellow-500">View Project</a>
            </div>

            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Project Three</h3>
              <p className="text-lg mb-4">A redesign of a social media website to enhance user engagement and im
</p>
</div>
</section>
</div>
</div>

)}