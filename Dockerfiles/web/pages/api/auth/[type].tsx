// import axios from "axios";
// import Cors from "cors";

// // Initializing the cors middleware
// const cors = Cors({
//     origin: "*",
//     methods: ["GET", "POST", "HEAD"]
// });

// // Helper method to wait for a middleware to execute before continuing
// // And to throw an error when an error happens in a middleware
// function runMiddleware(req, res, fn) {
//     return new Promise((resolve, reject) => {
//         fn(req, res, result => {
//             if (result instanceof Error) {
//                 return reject(result);
//             }

//             return resolve(result);
//         });
//     });
// }

// export default async (req, res) => {
//     // Run the middleware
//     await runMiddleware(req, res, cors);

//     console.log("HELLOOOOOOOOOOOOO");
//     const isAuth = await axios.get("http://localhost:8080/auth/login");

//     return res.status(200).json({
//         data: req.ssquery.type
//     });
// };
