// /app/api/hello/route.ts

import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    message: "Despliegue de Next.js en Vercel del Grupo 3",
  });
}
