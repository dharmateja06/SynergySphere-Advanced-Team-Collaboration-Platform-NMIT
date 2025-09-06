import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Projects from "./pages/Projects";
import ProjectDetail from "./pages/ProjectDetail";
import MyTasks from "./pages/MyTasks";
import CreateProject from "./pages/CreateProject";
import CreateTask from "./pages/CreateTask";

function App() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <main className="p-6">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/projects/:id" element={<ProjectDetail />} />
          <Route path="/my-tasks" element={<MyTasks task={{
            id: 0,
            title: "",
            status: ""
          }} />} />
          <Route path="/create-project" element={<CreateProject />} />
          <Route path="/create-task/:projectId" element={<CreateTask />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
