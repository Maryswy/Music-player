import Image from 'next/image';

// Sample data for genres
const genres = [
  { id: 1, name: 'Music', icon: '/music-icon.png' },
  { id: 2, name: 'Talk Shows', icon: '/talk-shows-icon.png' },
  { id: 3, name: 'News', icon: '/news-icon.png' },
  // Add more genres...
];

const BrowsePage = () => {
  return (
    <main>
      <section className="genres-list py-12">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-semibold mb-8">Browse by Genre</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {genres.map((genre) => (
              <div
                key={genre.id}
                className="bg-white p-4 rounded-md shadow-md flex flex-col items-center justify-center text-center"
              >
                <Image
                  src={genre.icon}
                  alt={`${genre.name} Icon`}
                  width={60}
                  height={60}
                />
                <h3 className="text-lg font-semibold mt-2">{genre.name}</h3>
                <a
                  href={`/genre/${genre.id}`}
                  className="bg-blue-600 text-white py-2 px-4 mt-4 rounded-md hover:bg-blue-800 transition duration-300 ease-in-out"
                >
                  Explore
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Add more content sections here */}
    </main>
  );
};

export default BrowsePage;
