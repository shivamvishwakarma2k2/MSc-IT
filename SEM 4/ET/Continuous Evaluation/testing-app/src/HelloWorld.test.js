import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import HelloWorld from './HelloWorld';

test('renders the heading', () => {
   render(<HelloWorld />);
   const element = screen.getByText(/hello/i);
   expect(element).toBeInTheDocument();
});

test('renders the subheading text', () => {
  render(<HelloWorld />)

  const subHeading = screen.getByText('From MSCIT part 2, Sem 4')
  expect(subHeading).toBeInTheDocument()
})

test('uses correct heading levels', () => {
  render(<HelloWorld />)

  const h1 = screen.getByRole('heading', { level: 1 })
  const h2 = screen.getByRole('heading', { level: 2 })

  expect(h1).toHaveTextContent('Hello, I am Shivam Vishwakarma.')
  expect(h2).toHaveTextContent('From MSCIT part 2, Sem 4')
})