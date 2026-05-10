import { createClient } from "@supabase/supabase-js"

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseKey = import.meta.env.VITE_SUPABASE_ANON_KEY

// Create a mock client if credentials are not configured
const createMockClient = () => ({
  auth: {
    signInWithOAuth: () => Promise.reject(new Error("Supabase not configured")),
    getSession: () => Promise.resolve({ data: { session: null } }),
    onAuthStateChange: () => ({ data: { subscription: { unsubscribe: () => {} } } })
  }
})

export const supabase = (supabaseUrl && supabaseKey && supabaseUrl !== 'placeholder' && supabaseKey !== 'placeholder')
  ? createClient(supabaseUrl, supabaseKey)
  : createMockClient()