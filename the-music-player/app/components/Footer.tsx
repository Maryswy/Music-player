const Footer = () => {
  return (
    <footer className="bg-gradient-to-r from-gray-800 to-gray-900 text-white py-6">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap justify-between">
          <div className="w-full md:w-1/4 mb-4 md:mb-0">
            <img src="/logo.png" alt="Internet Radio & Podcast Indexing Platform" width={180} height={37} />
          </div>
          <div className="w-full md:w-1/2 mb-4 md:mb-0">
            <h3 className="text-lg font-semibold mb-2">About Us</h3>
            <p>
              The Internet Radio & Podcast Indexing Platform is your gateway to a world of free live radio channels and podcasts. Our platform combines cutting-edge technology with user-friendly design, making it easier than ever to explore content based on your interests.
            </p>
          </div>
          <div className="w-full md:w-1/4 mb-4 md:mb-0">
            <h3 className="text-lg font-semibold mb-2">Quick Links</h3>
            <ul>
              <li><a href="/" className="text-gray-300 hover:text-white transition duration-300 ease-in-out">Home</a></li>
              <li><a href="/browse" className="text-gray-300 hover:text-white transition duration-300 ease-in-out">Browse</a></li>
              <li><a href="/top-charts" className="text-gray-300 hover:text-white transition duration-300 ease-in-out">Top Charts</a></li>
              <li><a href="/about" className="text-gray-300 hover:text-white transition duration-300 ease-in-out">About Us</a></li>
            </ul>
          </div>
        </div>
        <div className="mt-4 border-t border-gray-400 pt-4">
          <p className="text-center text-gray-300">&copy; {new Date().getFullYear()} Internet Radio & Podcast Indexing Platform - All Rights Reserved</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
