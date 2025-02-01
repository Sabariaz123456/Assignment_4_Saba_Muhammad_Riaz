export default function Footer(){
    return(
              <footer className="bg-gray-700 text-yellow-600 py-8">
                <div className="container mx-auto px-4">
                  <div className="flex flex-col md:flex-row justify-between items-center md:items-start space-y-6 md:space-y-0">
                    <div className="text-center md:text-left">
                      <div className="text-4xl font-bold tracking-wide mb-2">
                        <a href="/" className="hover:text-gray-600 transition-colors">SabaMuhammadRiaz</a>
                      </div>
                      <p className="text-sm opacity-80">Your go-to solution for all things amazing.</p>
                    </div>
          
                    <div className="text-center md:text-left space-y-4">
                      <h3 className="font-semibold text-lg">Quick Links</h3>
                      <nav>
                        <a href="#" className="block hover:text-gray-200 transition-colors">Home</a>
                        <a href="#about" className="block hover:text-gray-200 transition-colors">About</a>
                        <a href="#services" className="block hover:text-gray-200 transition-colors">Services</a>
                        <a href="#contact" className="block hover:text-gray-200 transition-colors">Contact</a>
                      </nav>
                    </div>
          
                    <div className="text-center md:text-left space-x-6">
                      <h3 className="font-semibold text-lg">Follow Us</h3>
                      <div className="flex justify-center md:justify-start space-x-4">
                        <a href="#" className="hover:text-gray-200 transition-colors">
                          <i className="fab fa-facebook-f"></i>
                        </a>
                        <a href="#" className="hover:text-gray-200 transition-colors">
                          <i className="fab fa-twitter"></i>
                        </a>
                        <a href="#" className="hover:text-gray-200 transition-colors">
                          <i className="fab fa-linkedin-in"></i>
                        </a>
                        <a href="#" className="hover:text-gray-200 transition-colors">
                          <i className="fab fa-instagram"></i>
                        </a>
                      </div>
                    </div>
                  </div>
          
                  <div className="mt-8 text-center text-sm opacity-70">
                    <p>&copy; {new Date().getFullYear()} SabaMuhammadRiaz. All Rights Reserved.</p>
                  </div>
                </div>
              </footer>
            );
          }
 