import { Link } from "react-router-dom";

interface Props {
  project: { id: number; name: string; description: string };
}

function ProjectCard({ project }: Props) {
  return (
    <div className="bg-white p-4 shadow-md rounded">
      <h2 className="text-lg font-semibold">{project.name}</h2>
      <p>{project.description}</p>
      <div className="mt-2 flex justify-between">
        <Link to={`/projects/${project.id}`} className="text-blue-600">View</Link>
      </div>
    </div>
  );
}

export default ProjectCard;
