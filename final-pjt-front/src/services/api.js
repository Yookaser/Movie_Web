import axios from "axios";

const token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNWRhMjUzMmIzMTIzZGJiNzZmOTg1OTQ5Nzc4YjVhYiIsInN1YiI6IjYxMDM4NjFjNGYzM2FkMDAyZDhkZGQ4NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tjhKbWARbBgM_gbXbpkB4wumMaSElr1P7nnF53reoSA"

export default axios.create({
  baseURL: "https://api.themoviedb.org/3",
  headers: {
    Authorization: `Bearer ${token}`
  },
})