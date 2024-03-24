import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule],
  template: `
  <div class="category-buttons">
  <button (click)="selectCategory('mac')">Mac</button>
  <button (click)="selectCategory('iphone')">iPhone</button>
  <button (click)="selectCategory('watch')">Watch</button>
  <button (click)="selectCategory('ipad')">iPad</button>
  <button (click)="selectCategory(null)">All Products</button>
</div>
    <div *ngFor="let product of filteredProducts" class="product-container">
      <h3>
        <a class="name" [title]="product.name + ' details'">
          {{ product.name }}
        </a>
      </h3>
      <img [src]="product.image" alt="{{ product.name }}" width="300">
      <p class="description">
        <strong> Описание: </strong> {{ product.description }}
      </p>
      <p class="description">
         <strong>Цена -> </strong>{{ product.price }}
      </p>

      <a [href]="'https://wa.me/?text=Check%20out%20' + product.name + '%20at%20this%20link:%20' + product.buyLink"
         class="share-button">
         Написать в WhatsApp->
      </a>

      <a [href]="product.buyLink" class="buy-button">
         Заказать сейчас
      </a>
    </div>
  `,
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  products: any[] = [
    { name: 'Iphone 15 pro', category: 'iphone', description: 'iPhone 15 Pro, 256 ГБ, Natural Titanium, (MTV53)', price: 659990, image: '/assets/iphone15pro.webp', buyLink: "https://example.com/laptop" },
    { name: 'Iphone 15', category: 'iphone', description: 'iPhone 15, 128 ГБ, Чёрный, (MTP03)', price: 449990, image: '/assets/iphone15.webp', buyLink: "https://example.com/smartphone" },
    { name: 'Iphone 15 plus', category: 'iphone', description: 'iPhone 15 Plus, 128 ГБ, Чёрный, (MU0Y3)', price: 549990, image: '/assets/iphone15plus.webp', buyLink: "https://example.com/camera" },
    { name: 'MacBook Air', category: 'mac', description: 'MacBook Air 13.6" Apple M2 (8C CPU/8C GPU), 8 ГБ, 256 ГБ, Тёмная ночь, 2022 (MLY33)', price: 589990, image: '/assets/macAirM2.webp', buyLink: "https://example.com/camera" },
    { name: 'Iphone 14 pro', category: 'iphone', description: 'iPhone 14 Pro, 1 TB, Чёрный, (MQ2H3)', price: 929990, image: '/assets/iphone14pro.webp', buyLink: "https://example.com/camera" },
    { name: 'MacBook Pro', category: 'mac', description: 'MacBook Pro 14.2" Apple M3 Pro (11C CPU/14C GPU), 18 ГБ, 512 ГБ, Чёрный, 2023 (MRX33)', price: 1229990, image: '/assets/macProM3Pro.webp', buyLink: "https://example.com/camera" },
    { name: 'MacBook Air', category: 'mac', description: 'MacBook Air 15.3" Apple M2 (8C CPU/10C GPU), 8 ГБ, 512 ГБ, Серый космос, 2023 (MQKQ3)', price: 699990, image: '/assets/macAir15M2.webp', buyLink: "https://example.com/camera" },
  ];
  selectedCategory: string | null = null;

  get filteredProducts(): any[] {
    return this.selectedCategory
      ? this.products.filter(product => product.category === this.selectedCategory)
      : this.products;
  }

  selectCategory(category: string | null): void {
    console.log('Выбранная категория:', category);
    this.selectedCategory = category;
  }

  share(product: any) {
    const message = `Check out ${product.name} at this link: ${product.buyLink}`;
    const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');
  }

  buy(link: string) {
    console.log('Buy link:', link);
    window.open(link, '_blank');
  }
}
