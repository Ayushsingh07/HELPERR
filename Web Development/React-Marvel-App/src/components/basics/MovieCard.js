import React from "react";

const MovieCard = ({ MovieCard }) => {
  // console.log(MovieCard)

  return (
    <>
      <section className="main-card--cointainer">
        {MovieCard.map((e) => {
          return (
            <>
              <div className="card-container" key={e.id}>
                <div className="card">
                  <div className="card-body">
                    <span className="card-number card-circle subtle">
                      {e.id}
                    </span>
                    <span className="card-author subtle">{e.category}</span>
                    <h2 className="card-title">{e.name}</h2>
                    <span className="card-description subtle">
                      <div className="card-read">Read</div>
                      {e.description}
                    </span>
                  </div>
                  <img src={e.image} alt="images" className="card-media" />
                  {/* <span className="card-tag subtle">Order Now</span> */}
                </div>
              </div>
            </>
          );
        })}
      </section>
      
     
    </>
  );
};

export default MovieCard;
