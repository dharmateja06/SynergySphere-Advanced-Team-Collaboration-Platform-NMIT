import { Link } from "react-router-dom";
import ProjectCard from "../components/Projectcards";

const sampleProjects = [
  { id: 1, name: "Website Redesign", description: "Improve UI/UX" },
  { id: 2, name: "Mobile App", description: "React Native app" },
];

function Projects() {
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h2 className="text-2xl font-bold">Projects</h2>
        <Link to="/create-project" className="bg-blue-600 text-white px-3 py-2 rounded">
          + New Project
        </Link>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {sampleProjects.map((p) => <ProjectCard key={p.id} project={p} />)}
      </div>
    </div>
  );
}

export default Projects;
