// Commentthread.tsx
import * as React from "react";
import { useState } from "react";

export type Comment = {
  id: number;
  body: string;
  replies?: { id: number; body: string }[];
};

export type CommentThreadProps = {
  comments: Comment[];           // <-- This is the correct prop name
  onAdd: (comment: Comment) => void;
  projectId: number;
};

const Commentthread: React.FC<CommentThreadProps> = ({ comments, onAdd, projectId }) => {
  const [body, setBody] = useState("");

  return (
    <div>
      {comments.map((c) => (
        <p key={c.id}>{c.body}</p>
      ))}
    </div>
  );
};

export default Commentthread;
