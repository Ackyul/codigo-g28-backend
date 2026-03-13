import type { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET;

export interface AuthRequest extends Request {
    user?: {
        id: number;
        email: string;
        rol: string;
    };
}

export function authMiddleware(
    req: AuthRequest,
    res: Response,
    next: NextFunction
) {
    // Leer el token que envia el cliente
    const authHeader = req.headers["authorization"];

    if (!authHeader) {
        return res.status(401).json({ ok: false, message: "Token expirado"});
    }
}