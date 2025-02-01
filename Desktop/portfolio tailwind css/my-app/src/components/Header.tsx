import Link from "next/link";

export default function Header() {
   
  
    return (
      <div>
        <header className="bg-gray-700 text-yellow-500 text-bold shadow-lg">
          <div className="container mx-auto px-4 py-4 flex justify-between items-center">
            <div className="text-3xl font-bold tracking-wide">
              <a href="/" className="hover:text-gray-200 transition-colors">
                SabaMuhammadRiaz
              </a>
            </div>
              <nav className="hidden md:flex space-x-8 text-lg">
              <Link href="/"> <li className="hover:text-gray-200 transition-colors">Home</li></Link>
              <Link href="/About"><li className="hover:text-gray-200 transition-colors">About</li></Link>
              <Link href="/contact"><li className="hover:text-gray-200 transition-colors">Contact</li></Link>
         
  </nav>
          
       </div>
       </header>
       </div>
    );
  }
  