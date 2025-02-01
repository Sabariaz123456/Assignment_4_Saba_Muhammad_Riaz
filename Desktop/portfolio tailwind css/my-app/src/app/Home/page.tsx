'use client'
import Image from "next/image";
import { useEffect } from "react";
import AOS from "aos";
import "aos/dist/aos.css"; // import AOS styles

export default function HomePage() {
  useEffect(() => {
    AOS.init({ duration: 1000, easing: 'ease-in-out' });
  }, []);

  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-pink-400 to-blue-800 text-white h-screen flex flex-col justify-center items-center text-center px-4 relative">
        {/* Background Image with Blur */}
        <div className="absolute inset-0 bg-cover bg-center blur-lg opacity-50" style={{ backgroundImage: "url('https://source.unsplash.com/1600x900/?technology,web')" }}></div>
        
        <div className="container mx-auto flex flex-col md:flex-row-reverse items-center justify-center px-4 relative z-10">
          {/* Profile Image with Rotate Animation */}
          <div
            className="w-64 h-64 md:w-80 md:h-80 mb-6 md:mb-0 rounded-full overflow-hidden border-4 border-white shadow-2xl transform transition-all duration-300 ease-in-out animate-rotate"
            data-aos="zoom-in"
          >
            <Image
              src="https://th.bing.com/th/id/OIP.EGdAQC3bQhaVlHbBqKkZjwAAAA?rs=1&pid=ImgDetMain"
              alt="Profile picture of Saba Riaz"
              className="w-full h-full object-cover"
            />
          </div>

          {/* Text Content */}
          <div className="text-center md:text-left md:ml-8 space-y-4 px-6" data-aos="fade-up">
            <h1 className="text-4xl md:text-6xl font-extrabold leading-tight mb-4 text-yellow-400">
              Hi, I m <span className="text-yellow-400">Saba Riaz</span>
            </h1>
            <p className="text-lg md:text-2xl mb-6 opacity-90">
              Hi! I m a passionate UI/UX Designer. I focus on creating seamless and beautiful user experiences.
              <br></br> I believe in a user-centered approach to design, solving real-world problems with creative solutions.
            </p>
            <a href="#contact" className="bg-yellow-400 text-gray-900 px-6 py-3 rounded-full text-lg font-semibold shadow-lg hover:bg-yellow-500 transition-colors duration-300" data-aos="fade-up" data-aos-delay="300">
              Get in Touch
            </a>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-16 bg-gray-900 text-white text-center" data-aos="fade-up">
        <h2 className="text-3xl md:text-4xl font-extrabold mb-8">Lets Work Together</h2>
        <p className="text-lg mb-6 opacity-80">
          Interested in collaborating on a project or want to learn more about my work? Feel free to reach out!
        </p>
        <a href="mailto:email@example.com" className="bg-yellow-400 text-gray-900 px-8 py-4 rounded-full text-lg font-semibold hover:bg-yellow-500 transition-colors duration-300" data-aos="fade-up" data-aos-delay="600">
          Contact Me
        </a>
      </section>
    </div>
  );
}
