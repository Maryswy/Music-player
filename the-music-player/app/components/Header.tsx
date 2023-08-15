"use client";
import Link from 'next/link';
import { useState } from 'react';
import Image from 'next/image';

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const linkClass = "text-lg text-white hover:text-blue-600 transition duration-300 ease-in-out p-2 rounded-md";

  return (
    <header className="flex flex-wrap justify-between items-center py-4 px-8 shadow-lg text-gray-800 font-medium tracking-wide bg-gradient-to-l from-gray-800 to-gray-900">
      <div className="flex flex-row items-center justify-between w-full md:w-auto m-auto">
        <Image
          src="/logo.png"
          alt="Internet Radio & Podcast Indexing Platform"
          width={150}
          height={50}
          objectFit="contain"
        />
        <button
          onClick={() => setMenuOpen(!menuOpen)}
          className="md:hidden focus:outline-none rounded-full bg-gray-800 text-white hover:text-blue-600 transition duration-300 ease-in-out"
          aria-label="Toggle Menu"
        >
          <Image src="/menu.svg" alt="Menu" width={50} height={50} />
        </button>
      </div>
     
      <nav className={`flex flex-col md:flex-row md:justify-around space-x-0 md:space-x-8 ${menuOpen ? 'block' : 'hidden'} md:block`}>
        <Link href="/" className={linkClass}>Home</Link>
        <Link href="/browse" className={linkClass}>Browse</Link>
        <Link href="/top-charts" className={linkClass}>Top Charts</Link>
        <Link href="/about" className={linkClass}>About Us</Link>
      </nav>
    </header>
  );
};

export default Header;
