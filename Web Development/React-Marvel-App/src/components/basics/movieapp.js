import React from "react";
import "./styles.css";
import MovieCard from "./MovieCard";
import Movie from "./movieapi";

const MovieApp = () => {
  // const [movieData, setMovieData] = React.useState(Movie);
  const [filterData, setfilterData] = React.useState("");
  // console.log(filterData);
  // console.log(Movie)
  // console.log(movieData)
  // const filteritem = (category) => {
  //   const updatesList = Movie.filter((e) => {
  //     return e.category === category;
  //   });
  //   setMovieData(updatesList);
  // };

  // const filtermovie = (moviename) => {
  //   console.log(moviename);
  //   const updates1List = Movie.filter((e) => {
  //     if (moviename == "") {
  //       console.log("empty");
  //     } else if (e.name.toLowerCase().includes(moviename.toLowerCase())) {
  //       // console.log(e.name);
  //     }
  //   });
  //   setfilterData(updates1List);
  // };
  return (
    <>
      <header>
        <h1> Marvel Phase-Wise Movies</h1>
      </header>
      <div className="input">
        <input
          type="text"
          placeholder="Search Name or phase"
          onChange={(e) => setfilterData(e.target.value)}
        />
      </div>
      {Movie.filter((val)=>{
        if(filterData=="")
        {
          return val;
        }
        else if(val.name.toLowerCase().includes(filterData.toLowerCase()) || val.category.toLowerCase().includes(filterData.toLowerCase()))
        {
          return val;
        }
      }).map((e, key) => {
        
        return (
          <>
          <section className="main-card--cointainer">
            <div className="card-container" key={e.id}>
              <div className="card">
                <div className="card-body">
                  <span className="card-number card-circle subtle">
                    {e.id}
                  </span>
                  <span className="card-author subtle">{e.category}</span>
                  <h2 className="card-title">{e.name}</h2>
                  <h3>{e.date}</h3>
                  <span className="card-description subtle">
                    <div className="card-read">Read</div>
                    {e.description}
                  </span>
                </div>
                {/* <img src={e.image} alt="images" className="card-media" /> */}
                {/* <span className="card-tag subtle">Order Now</span> */}
              </div>
            </div>
            </section>
          </>
        );
      })}

      {/* <nav className="navbar">
        <div className="btn-group">
          <button
            className="btn-group__item"
            onClick={() => filteritem("Phase 1")}
          >
            Phase 1
          </button>
          <button
            className="btn-group__item"
            onClick={() => filteritem("Phase 2")}
          >
            Phase 2
          </button>
          <button
            className="btn-group__item"
            onClick={() => filteritem("Phase 3")}
          >
            Phase 3
          </button>
          <button
            className="btn-group__item"
            onClick={() => filteritem("Phase 4")}
          >
            Phase 4
          </button>
        </div>
      </nav>
      <MovieCard MovieCard={movieData} /> */}
    </>
  );
};

export default MovieApp;
