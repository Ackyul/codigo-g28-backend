import type { Request, Response } from "express";
import { ProductService } from "../services/product.service";
import { Request, Response } from "undici-types";
import { ok } from "node:assert";

// instanciar ProductService
const service = new ProductService()

export class ProductController {
    // getAll
    async getAll(req:Request, res:Response) {
        try {    
            const products = await service.getAll();        
        } catch (error: any) {
            res.status(500).json({ ok:false, error: error.message});
        }
    }
}