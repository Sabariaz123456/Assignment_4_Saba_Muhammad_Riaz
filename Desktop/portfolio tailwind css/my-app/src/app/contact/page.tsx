"use client"
        import React, { useState } from 'react';

      export default function ContactPage() {
        const [formData, setFormData] = useState({
          name: "",
          email: "",
          message: ""
        });
        
        const [formSubmitted, setFormSubmitted] = useState(false);
      
        const handleChange = (e: { target: { name: any; value: any; } }) => {
          const { name, value } = e.target;
          setFormData({
            ...formData,
            [name]: value
          });
        };
      
        const handleSubmit = (e: { preventDefault: () => void; }) => {
          e.preventDefault();
          // Simulate form submission
          console.log(formData);
          setFormSubmitted(true);
          // Here, you would typically handle form submission, such as sending the data to a backend API or email service.
        };
      
        return (
          <div>
            <section className="bg-gradient-to-r from-pink-200 to-blue-300 text-pink h-screen flex flex-col justify-center items-center text-center px-4 py-8">
              <div className="container mx-auto max-w-4xl px-4">
                <h1 className="text-4xl font-extrabold mb-6 text-gray-400">Contact Me</h1>
                
                {/* Contact Form */}
                <form onSubmit={handleSubmit} className="space-y-6 bg-white p-6 rounded-lg shadow-lg">
                  <div>
                    <label htmlFor="name" className="block text-lg font-medium text-gray-700">Name</label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      className="w-full p-3 mt-2 border border-gray-300 rounded-md"
                      placeholder="Your Name"
                      required
                    />
                  </div>
      
                  <div>
                    <label htmlFor="email" className="block text-lg font-medium text-gray-700">Email</label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      className="w-full p-3 mt-2 border border-gray-300 rounded-md"
                      placeholder="Your Email"
                      required
                    />
                  </div>
      
                  <div>
                    <label htmlFor="message" className="block text-lg font-medium text-gray-700">Message</label>
                    <textarea
                      id="message"
                      name="message"
                      value={formData.message}
                      onChange={handleChange}
                      className="w-full p-3 mt-2 border border-gray-300 rounded-md"
                      placeholder="Your Message"
                      
                      required
                    ></textarea>
                  </div>
      
                  <div className="text-center">
                    <button type="submit" className="px-6 py-3 bg-yellow-400 text-white font-bold rounded-md hover:bg-yellow-500 transition-all">
                      Send Message
                    </button>
                  </div>
                </form>
      
                {/* Success Message */}
                {formSubmitted && (
                  <div className="mt-6 p-4 bg-green-100 text-green-700 rounded-md">
                    <p>Thank you for reaching out! I will get back to you as soon as possible.</p>
                  </div>
                )}
      
                {/* Contact Details */}
                <div className="mt-8">
                  <h2 className="text-2xl font-semibold text-gray-600">Other Ways to Reach Me</h2>
                  <p className="text-lg text-gray-500 mt-4">
                    If you prefer, you can also contact me through the following methods:
                  </p>
                  <ul className="mt-4 space-y-2">
                    <li className="text-lg text-gray-500">📧 Email: <span className="text-yellow-400">saba.riaz@example.com</span></li>
                    <li className="text-lg text-gray-500">📱 Phone: <span className="text-yellow-400">+123 456 7890</span></li>
                    <li className="text-lg text-gray-500">💼 LinkedIn: <span className="text-yellow-400">linkedin.com/in/sabariaz</span></li>
                  </ul>
                </div>
              </div>
            </section>
            <br></br>
            <br></br>
            <br></br>
          </div>
        );
      }
      
