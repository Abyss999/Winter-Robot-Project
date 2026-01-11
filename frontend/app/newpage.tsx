import { IMAGES_MANIFEST } from "next/dist/shared/lib/constants";
import Image from "next/image";

export default function NewPage() {
  return (
    <div>
        <main className="min-h-screen bg-white text-black dark:bg-black dark:text-white flex items-center justify-center">
        <div className="max-w-2xl p-8 space-y-4">
            <h1 className="text-3xl font-semibold">Winter Robot Project Type shiii</h1>
        </div>
        <div>
            <h2>Controls</h2>    
            <p>Controls:
                W - Move forward
                A - Move left
                S - Move backward
                D - Move right
            </p>
        </div>
        </main>
    </div>
  );
}