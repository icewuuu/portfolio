import { useEffect, useState } from "react";
import "./App.css";
import Nav from "./components/Nav";

function App() {
  const [educations, setEducation] = useState([]);
  const [works, setWork] = useState([]);
  const [certificates, setCertificates] = useState([]);
  const [portfolios, setPortfolios] = useState([]);

  useEffect(() => {
    getData();
  }, []);

  const getData = async () => {
    const educationRequest = fetch("/education").then((response) =>
      response.json()
    );
    const workRequest = fetch("/work").then((response) => response.json());
    const certificatesRequest = fetch("/certificates").then((response) =>
      response.json()
    );
    const portfoliosRequest = fetch("/portfolio").then((response) =>
      response.json()
    );

    Promise.all([
      educationRequest,
      workRequest,
      certificatesRequest,
      portfoliosRequest,
    ])
      .then(([educationData, workData, certificatesData, portfoliosData]) => {
        setEducation(educationData);
        setWork(workData);
        setCertificates(certificatesData);
        setPortfolios(portfoliosData);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  console.log(portfolios);
  return (
    <>
      <Nav />
      <div className="h-screen">
        <div className="w-2/4 mx-auto mt-10 mb-3">
          <h1 className="text-5xl mb-3">Piotr Marczak</h1>
        </div>
        <div className="w-2/4 mx-auto mt-10 mb-3">
          {works.map((work) => (
            <div key={work.id} className="bg-stone-100 p-4 mb-4">
              <h1 className="text-xl font-bold">{work.company}</h1>
              <p className="text-gray-600">{work.years}</p>
              <p className="mt-2">{work.description}</p>
            </div>
          ))}
        </div>

        <div className="w-2/4 mx-auto mt-10 mb-3">
          {portfolios.map((portfolio) => (
            <div key={portfolio.id} className="bg-stone-100 p-4 mb-4">
              <h1 className="text-xl font-bold">{portfolio.title}</h1>
              <img
                src={portfolio.image}
                alt={portfolio.title}
                className="mt-2"
              />
              <p className="mt-2">{portfolio.description}</p>
              <a href={portfolio.url} className="text-blue-500">
                {portfolio.url}
              </a>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default App;
